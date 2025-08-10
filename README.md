# 📚 Library Management System

A complete library management system with both **CLI** and **REST API** interfaces. Add books by ISBN, manage your collection, and access data through a web API.

Created as part of the Global AI Hub Python 202 Bootcamp to improve my Python skills and to practice OOP, API integration and FastAPI development.

## 🎯 What This Project Does
- **Add books by ISBN** - Just enter an ISBN, get title and author automatically from Open Library
- **Manage your collection** - Add, remove, list, and search books  
- **Two ways to use** - Command line interface OR web API
- **Persistent storage** - All data saved in JSON file
- **Fully tested** - Complete test suite with pytest

## 🚀 How to Run This Project

### ⚡ Super Quick Start (3 steps)
1. **Download**: `git clone https://github.com/AbdullahOztoprak/Global-AI-Hub-Python-202-Bootcamp-Project.git`
2. **Install**: `cd Global-AI-Hub-Python-202-Bootcamp-Project && pip install -r requirements.txt`
3. **Run**: Choose one option below 👇

### Option A: 🖥️ Command Line Interface
```bash
python main.py
```
- Follow the menu to add books by ISBN
- Try ISBN: `978-0439023528` for testing

### Option B: 🌐 Web API Server
```bash
uvicorn api:app --reload
```
- Open: http://127.0.0.1:8000/docs 
- Click "Try it out" to test endpoints
- Use POST `/books` with `{"isbn": "978-0439023528"}`

## 📋 API Endpoints
- `GET /books` - List all books
- `POST /books` - Add book by ISBN (e.g., `{"isbn": "978-0439023528"}`)
- `DELETE /books/{isbn}` - Remove a book

## 🧪 Testing
```bash
python -m pytest  # Run all tests
python -m pytest --cov  # Run with coverage
```

## 💡 Example Usage
1. **Add a book**: Enter ISBN `978-0439023528` (The Hunger Games)
2. **List books**: See your collection  
3. **API**: Visit `/docs` for interactive testing

## 🛠️ Tech Stack
- Python 3.12+
- FastAPI (REST API)
- httpx (API calls)
- Pydantic (data models)
- pytest (testing)

## 📁 Project Structure
```
book.py         # Book class
library.py      # Library class and persistence logic
main.py         # CLI application
api.py          # FastAPI application
library.json    # Data storage
tests/          # Unit tests
requirements.txt# Project dependencies
```

## 📝 License
This project is provided for educational purposes. 🎓
python -m pytest --cov=. --cov-report=term --cov-config=.coveragerc
```


## Project Structure
```
book.py         # Book class
library.py      # Library class and persistence logic
main.py         # CLI application
library.json    # Data storage
tests/          # Unit tests
.coveragerc     # Coverage configuration
```


## License
This project is provided for educational purposes. 🎓
