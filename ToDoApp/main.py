# ============================================================
#                           IMPORTS
# ============================================================
from fastapi import FastAPI

import models
from database import engine
from routers import auth, todos, admin, users


# ============================================================
#                    APP INITIALIZATION
# ============================================================
app = FastAPI()


# ============================================================
#                    DATABASE INITIALIZATION
# ============================================================
models.Base.metadata.create_all(bind=engine)


# ============================================================
#                    ROUTER REGISTRATION
# ============================================================
app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)
