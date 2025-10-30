# 🧱 Dev Template Repository

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Code style: Pylint](https://img.shields.io/badge/code%20style-pylint-000000.svg)](https://github.com/pylint-dev/pylint)

A comprehensive, production-ready template repository for initializing new development projects with consistent tooling, editor settings, GitHub workflows, and best practices. This template serves as a **baseline setup** for modern development workflows, reducing setup overhead and promoting standardization across all your codebases.

## 🎯 Overview
This template provides a solid foundation for Python projects with:
- **Pre-configured development environment** with VS Code settings and extensions
- **Automated CI/CD pipelines** using GitHub Actions
- **Code quality enforcement** with linting, formatting, and testing
- **Professional project structure** with proper documentation and metadata
- **Team collaboration tools** including PR templates and code ownership

---

## 📁 What's Included

### 🔧 Development Environment (`.vscode/`)
- **`settings.json`**: Editor defaults (format on save, lint integration, tab size, Python interpreter)
- **`extensions.json`**: Recommended extensions for Python development and team consistency
- **`keybindings.json`**: Custom keyboard shortcuts for improved productivity
- **`launch.json`**: Debugging configurations for Python applications

### ⚙️ GitHub Configuration (`.github/`)
- **Workflows**: Automated CI/CD pipelines for testing, linting, and publishing
  - `publish_to_pypi.yml`: Automated PyPI package publishing
- **`CODEOWNERS`**: Define default code reviewers per folder/path
- **Issue templates**: Standardized bug reports and feature requests
- **Pull request template**: Enforce contribution guidelines and checklists

### 🧹 Code Quality & Style
- **Python-specific configurations**:
  - `requirements.txt`: Core dependencies and development tools
  - `MANIFEST.in`: Package distribution configuration
  - `env.template`: Environment variables template
- **`.gitignore`**: Preconfigured for Python, IDEs, and common tools
- **`.cursor/`**: Cursor IDE specific configurations and instructions

### 📄 Project Metadata
- **`README.md`**: Comprehensive project documentation
- **`LICENSE`**: MIT license for open-source projects
- **`CHANGELOG.md`**: Version tracking and release notes

---

## 🚀 Quick Start

### 1. Create New Repository
Click **"Use this template"** on GitHub to create a new repository based on this template.

### 2. Clone and Setup
```bash
# Clone your new repository
git clone https://github.com/your-username/your-new-repo.git
cd your-new-repo

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp env.template .env
# Edit .env with your specific configuration
```

### 3. Customize for Your Project
1. **Update project metadata**:
   - Edit `README.md` with your project details
   - Update `requirements.txt` with your specific dependencies
   - Modify `MANIFEST.in` for package distribution

2. **Configure environment**:
   - Edit `.env` file with your environment variables
   - Update VS Code settings in `.vscode/settings.json` if needed

### 4. Setup Pre-commit Hooks
```bash
# Install pre-commit hooks
pre-commit install
```

```bash
# Run on all files (optional, for existing codebase)
pre-commit run --all-files
```

```bash
# Run on all files excluding specific files (example: main.py) (optional, for existing codebase)
pre-commit run --files $(git ls-files | grep -v "main.py")
```

**Automatic Usage:**
Once installed, pre-commit will automatically run on every `git commit`. If any hook fails:
- **Fix the issues** and commit again
- **Skip hooks** (not recommended): `git commit --no-verify`

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Ensure all tests pass: `pytest`
5. Format your code: `black .`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

---

## 📋 Development Checklist
When using this template for a new project:

- [ ] Update README.md with project-specific information
- [ ] Configure environment variables in .env
- [ ] Update requirements.txt with project dependencies
- [ ] Set up GitHub repository secrets for CI/CD
- [ ] Configure package metadata in setup.py or pyproject.toml
- [ ] Add project-specific tests

---
