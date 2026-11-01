from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables
from routes import books, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Databse tables created")
    yield
    print("Application shutdown.")


app = FastAPI(
    title="Kitaab Exchange API",
    description="A simple API for exchanging used books.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(users.router)
app.include_router(books.router)


@app.get("/")
def root():
    return {
        "Message":"Kitaab exchange API is serving successfully",
        "status_code":"200"
    }