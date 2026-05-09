from fastapi import FastAPI

app = FastAPI(title="DocManager API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "DocManager API is running"}
