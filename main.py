from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "Message":"Kitaab exchange API is serving successfully",
        "status_code":"200"
    }