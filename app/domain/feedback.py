import random

def skai_feedback(label: str, confidence: float) -> str:
    templates_high = [
        f"I’m quite confident this is a {label}. The lines feel intentional.",
        f"Looks like a {label}! I really like how you’re exploring shapes."
    ]
    templates_med = [
        f"This seems like a {label}. Keep experimenting with your forms.",
        f"I think this could be a {label}. Interesting strokes!"
    ]
    templates_low = [
        "I'm not entirely sure what this is, but I enjoy your direction.",
        "Hmm, this is tricky, but keep going! I like your energy."
    ]

    if confidence > 0.8:
        return random.choice(templates_high)
    elif confidence > 0.6:
        return random.choice(templates_med)
    else:
        return random.choice(templates_low)