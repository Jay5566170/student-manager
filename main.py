import importlib

from fastapi import FastAPI
from database import engine
from models import Base
from routes import students

try:
    auth_routes = importlib.import_module("routes.auth")
except ModuleNotFoundError:
    auth_routes = None

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Manager API (PostgreSQL)",
    description="Complete CRUD API with SQLAlchemy + PostgreSQL",
    version="1.0.0"
)

# Include routes
app.include_router(students.router)
if auth_routes is not None and hasattr(auth_routes, "router"):
    app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Student Manager API with PostgreSQL", "docs": "/docs"}