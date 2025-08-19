# 📚 Library Management System

A complete library management system with both CLI and REST API interfaces. Add books by ISBN, manage your collection, and access data through a web API.

Created as part of the Global AI Hub Python 202 Bootcamp to practice OOP, API integration and FastAPI development.

## 🎯 Features

- Add books by ISBN with automatic title and author fetching from Open Library
- Manage your collection: add, remove, list, and search books
- Two interfaces: command line application and web API
- Persistent storage with SQLite database (no more JSON file!)
- Complete test suite with pytest

## 📸 Screenshots

Below are some screenshots to show how the web frontend looks:

- **Library Homepage**
  ![Library View](assets/Screenshot(4).png)

- **Search Area**
  ![Search Bar](assets/Screenshot(5).png)

- **Add / Update / Delete Book Area**
  ![Book Management Area](assets/Screenshot(6).png)

  - **Tests**
  ![pytest tests](assets/Screenshot(7).png)

  
## 🚀 Installation

### Prerequisites
- **Python 3.8+** (recommended: Python 3.11 or 3.12) - [Microsoft Store](ms-windows-store://search/?query=python) or [python.org](https://python.org/downloads/)
- Git (optional, for cloning)

### Step 0: Install Python (If Not Already Installed)

**Option 1: Microsoft Store (Recommended for Windows)**
1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Install the latest version (Python 3.11 or 3.12)
4. Verify installation by opening PowerShell and running:
   ```powershell
   python --version
   ```

**Option 2: Official Python Website**
1. Go to https://python.org/downloads/
2. Download Python 3.11+ or 3.12+ for Windows
3. **Important:** During installation, check "Add Python to PATH"
4. Verify installation by opening PowerShell and running:
   ```powershell
   python --version
   ```
   or
   ```powershell
   py --version
   ```

### Step 1: Clone Repository
```powershell
git clone https://github.com/AbdullahOztoprak/Global-AI-Hub-Python-202-Bootcamp-Project.git
cd Global-AI-Hub-Python-202-Bootcamp-Project
```

**Or download as ZIP:**
1. Download the project as ZIP from GitHub
2. Extract to a folder
3. Open PowerShell in that folder

### Step 2: Install Dependencies

**Option A: With Virtual Environment (Recommended)**
```powershell
# Create virtual environment
python -m venv .venv

# Activate it (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Option B: Without Virtual Environment (Global Installation)**
```powershell
# Install directly to your system Python
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Note:** If you choose Option A, remember to activate the virtual environment every time you work on the project.

**Alternative:** If `python` command doesn't work, try replacing `python` with `py` in all commands above.

### 🔧 Troubleshooting Installation

**If you get "python not found" error:**
1. Install Python from https://python.org/downloads/
2. Make sure to check "Add Python to PATH" during installation
3. Restart PowerShell after installation
4. Try using `py` instead of `python`

**If you get "pip not found" error:**
- Use `python -m pip` instead of `pip`
- Or use `py -m pip` instead of `pip`

**If PowerShell execution policy prevents activation:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**If pip install fails:**
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**If you still have issues:**
- Try using `py` instead of `python` in all commands
- Make sure you're in the correct project directory

## 🖥️ Usage

**If you used a virtual environment, activate it first:**
```powershell
.\.venv\Scripts\Activate.ps1
```

### Command Line Interface
```powershell
python main.py
```
Follow the menu options to manage your library. Try adding a book with ISBN: `978-0439023528`

### Web API Server
```powershell
python -m uvicorn api:app --reload
```
- Open http://127.0.0.1:8000/docs in your browser for interactive API documentation
- The API will be available at http://localhost:8000
- Press `Ctrl+C` to stop the server

### Web Frontend
**Important:** The API server must be running first!

1. Start the API server (see above)
2. Go to the `web` folder in your project directory
3. Open `index.html` in your browser (double-click, right-click and select 'Open with browser' or drag the file into your browser window to open it in a new tab)
4. Use the interface to add, update, and delete books

**Note:** The web frontend fetches data from your API at `http://localhost:8000`. Make sure the API server is running before using the web interface.

### 🔧 Common Usage Issues

**If you get "Module not found" errors:**
- If using virtual environment: Make sure it's activated
- If not using virtual environment: Reinstall dependencies globally: `pip install -r requirements.txt`

**If the web frontend doesn't work:**
- Ensure the API server is running at http://localhost:8000
- Check browser console (F12) for error messages
- Try refreshing the page

**If you get database errors:**
- The `library.db` file will be created automatically
- Delete `library.db` if you want to start with a fresh database


## 📋 API Endpoints

- `GET /books` - List all books in the library
- `POST /books` - Add a new book by ISBN
- `PUT /books/{isbn}` - Update book details (title and/or author)
- `DELETE /books/{isbn}` - Remove a book from the library


### Example API Usage
```json
POST /books
{
  "isbn": "978-0439023528"
}

PUT /books/978-0439023528
{
  "title": "New Title",
  "author": "New Author"
}
```

## 🧪 Testing

**Make sure your virtual environment is activated first!**

Run all tests:
```powershell
python -m pytest
```

Run tests with coverage:
```powershell
python -m pytest --cov
```

Run tests with detailed output:
```powershell
python -m pytest -v
```

## 🛠️ Tech Stack

- Python 3.12+
- FastAPI for REST API
- httpx for HTTP requests
- Pydantic for data validation
- pytest for testing
- SQLite for persistent storage
- HTML/CSS/JavaScript for web frontend

## 📁 Project Structure

```
book.py         # Book class definition
library.py      # Library class and SQLite persistence logic
main.py         # CLI application
api.py          # FastAPI application
library.db      # SQLite database file
web/index.html  # Web frontend interface
tests/          # Unit tests
requirements.txt# Project dependencies
```


## 📝 License

This project is provided for educational purposes.
