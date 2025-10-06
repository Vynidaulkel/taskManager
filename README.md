# 🗂️ Task Manager API

A **RESTful API** built with **FastAPI** to manage tasks efficiently.  
This project demonstrates the implementation of CRUD operations, data validation, and database persistence using modern Python frameworks and best practices — perfect for showcasing backend development skills.

---

## 🚀 Features
- **FastAPI** framework for high-performance API development  
- **CRUD operations** for creating, reading, updating, and deleting tasks  
- **SQLite + SQLAlchemy** for database management  
- **Pydantic** for data validation and serialization  
- **Pytest** automated tests to ensure endpoint reliability  
- Clear project structure with virtual environment and `.gitignore` setup  

---

## 🧱 Tech Stack
- **Language:** Python 3.12  
- **Framework:** FastAPI  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Validation:** Pydantic  
- **Testing:** Pytest  
- **Server:** Uvicorn  

---

## 🧩 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the API
python -m uvicorn app.main:app --reload
