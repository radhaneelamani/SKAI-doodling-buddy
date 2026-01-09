from app.domain.feedback import skai_feedback
from PIL import Image
from app.domain.inference import classify_sketch
from app.domain.visualization import add_overlay

def analyze_sketch(file):
    image = Image.open(file.file)
    label, confidence = classify_sketch(image)
    comment = skai_feedback(label, confidence)

    # Add overlay for frontend
    annotated_image = add_overlay(image)
    # Convert PIL to bytes for API
    from io import BytesIO
    import base64
    buffered = BytesIO()
    annotated_image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")


    return {
        "label": label,
        "confidence": confidence,
        "comment": comment,
        "annotated_image": img_str
    }
