from fastapi import FastAPI

app = FastAPI(title="Skai - Sketching AI")

@app.get("/")
def health_check():
    return {"status": "Skai is alive"}
