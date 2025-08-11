# 📚 Library Management System

A complete library management system with both CLI and REST API interfaces. Add books by ISBN, manage your collection, and access data through a web API.

Created as part of the Global AI Hub Python 202 Bootcamp to practice OOP, API integration and FastAPI development.

## 🎯 Features

- Add books by ISBN with automatic title and author fetching from Open Library
- Manage your collection: add, remove, list, and search books
- Two interfaces: command line application and web API
- Persistent storage with JSON file
- Complete test suite with pytest

## 🚀 Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/AbdullahOztoprak/Global-AI-Hub-Python-202-Bootcamp-Project.git
cd Global-AI-Hub-Python-202-Bootcamp-Project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🖥️ Usage

### Command Line Interface
```bash
python main.py
```
Follow the menu options to manage your library. Try adding a book with ISBN: `978-0439023528`

### Web API Server
```bash
uvicorn api:app --reload
```
Open http://127.0.0.1:8000/docs in your browser for interactive API documentation.

## 📋 API Endpoints

- `GET /books` - List all books in the library
- `POST /books` - Add a new book by ISBN
- `DELETE /books/{isbn}` - Remove a book from the library

### Example API Usage
```json
POST /books
{
  "isbn": "978-0439023528"
}
```

## 🧪 Testing

Run all tests:
```bash
python -m pytest
```

Run tests with coverage:
```bash
python -m pytest --cov
```

## 🛠️ Tech Stack

- Python 3.12+
- FastAPI for REST API
- httpx for HTTP requests
- Pydantic for data validation
- pytest for testing

## 📁 Project Structure

```
book.py         # Book class definition
library.py      # Library class and persistence logic
main.py         # CLI application
api.py          # FastAPI application
library.json    # Data storage file
tests/          # Unit tests
requirements.txt# Project dependencies
```

## 📝 License

This project is provided for educational purposes.
