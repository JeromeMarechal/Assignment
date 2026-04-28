# Language Flashcard Application - Setup & Launch Guide

## Overview

This is a Flask-based language learning application (Flashcard FR) that helps users learn French vocabulary through interactive flashcards and quizzes. The app includes user authentication, card management, a dashboard, and various quiz exercises.

## Author

- **Name:** Jérôme Maréchal
- **Project Start Date:** 28 September 2025
- **Inspiration/Purpose:** My work as a French teacher /[CS50 Final Project

## Features

- User authentication and registration
- Search and preview flashcards
- Create and manage flashcards
- Take interactive quizzes
- Track learning progress on a dashboard
- AI-powered word analysis

## How to Use the App

### Creating an Account
As you launch the app, you can create a new account by clicking on the "Register" button on the login page. Fill in your details and submit the form to create your account.

### Adding Flashcards
Navigate to the flashcard section by clicking on search in the main  menu. After having fill up the form in order to create a flashcard, click on search, a flashcard will be created ; then at the bottom of the card you will see two buttons 'add' or 'discard'. Click on 'add' to add the flashcard to your collection. 

### Taking a Quiz
To take a quiz, go to the quiz section from the main menu. Select the type of quiz you want to take and start the quiz. Answer the questions and submit your responses to see your score.

### Viewing Progress
You can view your learning progress on the dashboard. It provides insights into your performance, including the number of flashcards learned and quiz scores.

## Prerequisites

- Python 3.11+ (as specified in pyproject.toml)
- Poetry (Python package manager) - Install from [python-poetry.org](https://python-poetry.org)
- Git (for version control)
- SQLite3 (included with Python)
## Installation Steps

### 1. Clone or Navigate to Project 

```bash
cd flashcard_fr
```

### 2. Install Poetry (if not already installed)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Install Dependencies

Poetry will read from `pyproject.toml` and install all required packages:

```bash
poetry install
```

This installs:

- **Flask** (>=3.1.2) - Web framework
- **Flask-Login** (>=0.6.3) - User authentication
- **Flask-SQLAlchemy** (>=3.1.1) - ORM and database
- **Flask-Migrate** (>=4.1.0) - Database migrations
- **python-dotenv** (>=1.2.1) - Environment variable management
- **google-generativeai** (>=0.8.6) - AI-powered word analysis
- **mypy & types-requests** (dev dependencies) - Type checking

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URI=sqlite:///flashcards.db
```

### 5. Initialize the Database

```bash
poetry run flask --app app db upgrade
```

If migrations don't exist, initialize Alembic:

```bash
poetry run flask --app app db init
poetry run flask --app app db migrate -m "Initial migration"
poetry run flask --app app db upgrade
```

## Launching the Application

### Development Mode (with Auto-reload)

```bash
poetry run flask --app app run --debug
```

The application will start on http://localhost:5000

### Production Mode

```bash
poetry run flask --app app run
```

### Troubleshooting: Windows Security Blocks

If you encounter a `Device Guard` or `Application Control` error when running the app on Windows, it is because local `.exe` files in the virtual environment are being blocked.

### The Fix
Instead of the standard `poetry run`, use the **Python Module** path to bypass the block:

```bash
python -m poetry run python -m flask run --debug

## Project Structure Overview

| Directory/File | Purpose |
|---|---|
| `routes/` | API endpoints (auth, cards, dashboard, quiz) |
| `services/` | Business logic and services |
| `repositories/` | Data access layer (CRUD operations) |
| `templates/` | HTML templates (Flask Jinja2) |
| `static/` | CSS and frontend assets |
| `clients/` | External API clients (translation, AI) |
| `contents/` | Static content (languages by region) |
| `migrations/` | Database migration scripts (Alembic) |
| `utils/` | Helper functions and utilities |
| `models.py` | SQLAlchemy database models |
| `config.py` | Application configuration |

### Detailed Subdirectories

| Path | Description |
|---|---|
| `routes/auth_routes.py` | Authentication endpoints (login, register) |
| `routes/card_routes.py` | Flashcard CRUD endpoints |
| `routes/dashboard_routes.py` | Dashboard data endpoints |
| `routes/quiz_routes.py` | Quiz and exercise endpoints |
| `services/auth_service.py` | User authentication logic |
| `services/card_service.py` | Flashcard business logic |
| `services/dashboard_service.py` | Dashboard aggregation logic |
| `services/quiz_service.py` | Quiz exercise logic |
| `repositories/card/card_repository.py` | Card database operations |
| `repositories/user/user_repository.py` | User database operations |
| `repositories/quiz/quiz_repository.py` | Quiz database operations |
| `repositories/dashboard/dashboard_repository.py` | Dashboard data queries |
| `templates/auth/` | Login and registration pages |
| `templates/quiz_exercises/meaning/` | Quiz exercise templates |
| `templates/components/` | Reusable HTML components |
| `clients/translate.py` | Translation API client |
| `clients/prompt_error.py` | AI error analysis client |

## License

This project is licensed under the **MIT License** - Copyright (c) 2025 Jérôme Maréchal