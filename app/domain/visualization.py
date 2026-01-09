from PIL import Image, ImageDraw, ImageEnhance
import random

def add_overlay(image: Image.Image):
    """
    Adds a semi-transparent highlight overlay on random regions
    to simulate AI attention.
    """
    overlay = Image.new("RGBA", image.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)

    # simulate attention boxes
    for _ in range(3):
        x0 = random.randint(0, image.width//2)
        y0 = random.randint(0, image.height//2)
        x1 = x0 + random.randint(10, image.width//2)
        y1 = y0 + random.randint(10, image.height//2)
        draw.rectangle([x0,y0,x1,y1], outline=(0, 150, 255, 150), width=2)

    return Image.alpha_composite(image.convert("RGBA"), overlay)
