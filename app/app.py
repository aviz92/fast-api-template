from fastapi import FastAPI, HTTPException, Depends
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/posts")
async def create_post(
    post: PostCreate,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        post = Post(
            title=post.title,
            content=post.content
        )
        session.add(post)
        await session.commit()
        await session.refresh(post)
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/posts")
async def get_all_posts(
    limit: int = None,
    offset: int = 0,
    session: AsyncSession = Depends(get_async_session),
) -> list[dict]:
    result = await session.execute(select(Post).order_by(Post.id.asc()))
    posts = [row[0] for row in result.all()]

    posts_data = []
    for post in posts:
        posts_data.append(
            PostResponse(
                id=post.id,
                created_at=post.created_at.isoformat(),
                title=post.title,
                content=post.content,
            ).__dict__
        )
    return posts_data[offset: offset + limit if limit else None]


@app.get("/posts/{post_id}")
async def get_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        result = await session.execute(select(Post).where(Post.id == post_id))
        post = result.scalars().first()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        return PostResponse(
            id=post.id,
            title=post.title,
            content=post.content,
            created_at=post.created_at.isoformat(),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
