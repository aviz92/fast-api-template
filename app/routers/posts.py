from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import Post, User, get_async_session
from app.schemas import PostCreate, PostResponse
from app.users import current_active_user

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("")
async def create_post(
    post: PostCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    try:
        post = Post(title=post.title, content=post.content, user_id=user.id)
        session.add(post)
        await session.commit()
        await session.refresh(post)
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("", response_model=list[PostResponse])
async def get_all_posts(
    limit: int | None = None,
    offset: int = 0,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
) -> list[PostResponse]:
    result = await session.execute(select(Post).order_by(Post.id.asc()))
    posts = [row[0] for row in result.all()]

    posts_data = [
        PostResponse(
            id=post.id,
            created_at=post.created_at.isoformat(),
            title=post.title,
            content=post.content,
            user_id=post.user_id,
            id_owner=user.id == post.user_id,
        )
        for post in posts
    ]

    return posts_data[offset: offset + limit if limit else None]


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
) -> PostResponse:
    try:
        result = await session.execute(select(Post).where(Post.id == post_id))
        if not (post := result.scalars().first()):
            raise HTTPException(status_code=404, detail="Post not found")

        return PostResponse(
            id=post.id,
            title=post.title,
            content=post.content,
            created_at=post.created_at.isoformat(),
            user_id=post.user_id,
            id_owner=user.id == post.user_id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.delete("/{post_id}")
async def delete_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
) -> dict[str, Any]:
    try:
        result = await session.execute(select(Post).where(Post.id == post_id))
        if not (post := result.scalars().first()):
            raise HTTPException(status_code=404, detail="Post not found")

        if post.user_id != user.id:
            raise HTTPException(status_code=403, detail="You don't have permission to delete this post")

        await session.delete(post)
        await session.commit()

        return {"success": True, "message": "Post deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
