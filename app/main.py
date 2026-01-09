from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Skai - Sketching AI")
app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "Skai is alive"}
