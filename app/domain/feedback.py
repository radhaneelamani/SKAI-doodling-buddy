def skai_feedback(label: str, confidence: float) -> str:
    if confidence > 0.8:
        return f"I feel quite confident this is a {label}. The lines feel intentional and calm."
    elif confidence > 0.6:
        return f"This looks like a {label}. I like how you're exploring the shapes."
    else:
        return "I'm not entirely sure what this is yet, but I enjoy the direction you're taking."
