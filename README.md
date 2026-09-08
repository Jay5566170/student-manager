# Student Manager API

A complete REST API for managing student records, built with **FastAPI** and **PostgreSQL**. This project demonstrates the progression from a simple CLI tool to a production-ready API with database integration.

---

## 🚀 Features

- ✅ **CRUD Operations** — Create, Read, Update, Delete students
- ✅ **PostgreSQL Database** — Production-grade database integration
- ✅ **SQLAlchemy ORM** — Clean, maintainable database interactions
- ✅ **FastAPI** — Modern, fast web framework
- ✅ **Swagger UI** — Interactive API documentation (`/docs`)
- ✅ **Environment Variables** — Secure configuration with `.env`

---

## 🛠️ Tech Stack

| **Technology** | **Purpose** |
|----------------|-------------|
| Python 3.11+ | Programming language |
| FastAPI | Web framework |
| SQLAlchemy | ORM (Object-Relational Mapping) |
| PostgreSQL | Production database |
| Pydantic | Data validation |
| Uvicorn | ASGI server |

---

## 📂 Project Structure
student-manager/
├── routes/
│ ├── init.py
│ └── students.py # API endpoints
├── .env # Environment variables (not committed)
├── database.py # Database connection
├── main.py # FastAPI app
├── models.py # Database models
├── requirements.txt # Dependencies
├── run.py # Server launcher
└── schemas.py # Pydantic schemas

text

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL (or use SQLite for testing)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jay5566170/student-manager.git
   cd student-manager
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Create .env file:

env
DATABASE_URL=postgresql://username:password@localhost:5432/student_db
Run the server:

bash
python run.py
Open Swagger UI:

Go to http://127.0.0.1:8000/docs

📊 API Endpoints
Method	Endpoint	Description
GET	/students/	Get all students
POST	/students/	Create a new student
GET	/students/{id}	Get one student
PUT	/students/{id}	Update a student
DELETE	/students/{id}	Delete a student
📝 Example Request
Create a student:

json
POST /students/
{
  "name": "Ali",
  "age": 22,
  "city": "Lahore",
  "email": "ali@example.com"
}
Response:

json
{
  "id": 1,
  "name": "Ali",
  "age": 22,
  "city": "Lahore",
  "email": "ali@example.com"
}
📚 What I Learned
Building REST APIs with FastAPI

Database integration with PostgreSQL and SQLAlchemy

Environment variables for secure configuration

Project structure and separation of concerns

CRUD operations and API design

🔗 Links
GitHub: Jay5566170/student-manager

Live Demo: [Coming soon]

📄 License
This project is for learning purposes only.

text

---

