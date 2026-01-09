from app.domain.feedback import skai_feedback

def analyze_sketch(file):
    # For now: stub inference
    label = "abstract sketch"
    confidence = 0.75

    comment = skai_feedback(label, confidence)

    return {
        "label": label,
        "confidence": confidence,
        "comment": comment
    }
#TODO: Integrate actual ML model inference here in the future