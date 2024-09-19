from fastapi import FastAPI
from app.routers import user_router, item_router
from app.database.connection import engine
from app.models import user_model, item_model

app = FastAPI()

# Include routers
app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(item_router.router, prefix="/items", tags=["items"])

# Initialize database
from app.database.connection import Base
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}
