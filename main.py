from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

from database import engine
from models import Base
from routes import auth, students

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Manager API (PostgreSQL)",
    description="Complete CRUD API with SQLAlchemy + PostgreSQL + JWT Authentication",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

app.include_router(students.router)
app.include_router(auth.router)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    html = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_ui_parameters={"persistAuthorization": True},
    )
    body = html.body.decode()
    body = body.replace(
        "</body>",
        """
        <button id="clear-auth-btn" style="position:fixed;top:18px;right:18px;z-index:2000;background:#e11d48;color:white;border:none;border-radius:8px;padding:10px 14px;font-weight:600;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.15);">Clear Auth</button>
        <script>
            document.addEventListener('DOMContentLoaded', function () {
                const clearBtn = document.getElementById('clear-auth-btn');
                if (!clearBtn) return;

                clearBtn.addEventListener('click', function () {
                    const keys = [];
                    for (let i = 0; i < localStorage.length; i++) {
                        const key = localStorage.key(i);
                        if (key && (key.toLowerCase().includes('swagger') || key.toLowerCase().includes('authorization') || key.toLowerCase().includes('bearer'))) {
                            keys.push(key);
                        }
                    }
                    keys.forEach((key) => localStorage.removeItem(key));
                    if (window.ui && typeof window.ui.preauthorizeApiKey === 'function') {
                        window.ui.preauthorizeApiKey('httpBearer', '');
                    }
                    alert('Authorization cleared from Swagger UI');
                });
            });
        </script>
        </body>
        """,
    )
    return HTMLResponse(content=body)

@app.get("/")
def root():
    return {
        "message": "Student Manager API with PostgreSQL + JWT",
        "docs": "/docs"
    }