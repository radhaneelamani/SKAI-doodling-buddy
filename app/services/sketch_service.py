from app.domain.feedback import skai_feedback
from PIL import Image
from app.domain.inference import classify_sketch

def analyze_sketch(file):
    image = Image.open(file.file)
    label, confidence = classify_sketch(image)
    comment = skai_feedback(label, confidence)

    return {
        "label": label,
        "confidence": confidence,
        "comment": comment
    }
