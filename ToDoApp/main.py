# ============================================================
#                           IMPORTS
# ============================================================
from pathlib import Path

from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ToDoApp.database import engine
from ToDoApp.models import Base
from ToDoApp.routers import auth, todos, admin, users


# ============================================================
#                    APP INITIALIZATION
# ============================================================
app = FastAPI()


# ============================================================
#                    DATABASE INITIALIZATION
# ============================================================
Base.metadata.create_all(bind=engine)


# ============================================================
#                    PATHS & STATIC FILES
# ============================================================
BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

app.mount("/static",StaticFiles(directory=BASE_DIR / "static"),name="static")


# ============================================================
#                    ROOT & HEALTH ROUTES
# ============================================================
@app.get("/")
def root():
    return RedirectResponse(url="/todos/todo-page",status_code=status.HTTP_302_FOUND)


@app.get("/healthy")
async def healthy():
    return {"status": "Healthy"}


# ============================================================
#                    ROUTER REGISTRATION
# ============================================================
app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)
