from fastapi import APIRouter, UploadFile, File
from app.services.sketch_service import analyze_sketch

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = analyze_sketch(file)
    return result
