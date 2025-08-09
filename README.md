# Global-AI-Hub-Python-202-Bootcamp-Project
Created as part of the Global AI Hub Python 202 Bootcamp to improve my Python skills and to practice OOP, API integration and FastAPI development.


# Library Management System


## Overview
This project is a command-line library management system built with Python. It demonstrates object-oriented programming and persistent data storage using JSON. Automated unit tests are provided for reliability. 


## Features
- Add, remove, list, and search books
- Persistent storage in `library.json`
- Command-line menu interface
- OOP design with `Book` and `Library` classes
- Automated unit tests with pytest


## Installation & Usage
### 📥 Clone the repository
```sh
git clone https://github.com/AbdullahOztoprak/Global-AI-Hub-Python-202-Bootcamp-Project.git
```

### 🛠️ Install dependencies
```sh
pip install pytest pytest-cov
```

### ▶️ Run the application
```sh
python main.py
```

### 🧪 Run tests
```sh
python -m pytest
```

### 📊 Check code coverage
```sh
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
