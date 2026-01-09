import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# Minimal CNN stub for demo (replace with real model later)
class DummySketchClassifier(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.fc = nn.Linear(1, num_classes)

    def forward(self, x):
        # returns random logits for demonstration
        return torch.rand((x.shape[0], 10))

# Initialize model (singleton for now)
model = DummySketchClassifier()
model.eval()

# Map index → label (10 example classes)
LABELS = ["apple", "house", "tree", "car", "boat", "cat", "dog", "sun", "flower", "abstract"]

# Transform input image
transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

def classify_sketch(image: Image.Image):
    x = transform(image).unsqueeze(0)  # shape [1,1,28,28]
    with torch.no_grad():
        logits = model(x)
        probs = torch.softmax(logits, dim=1)
        confidence, idx = torch.max(probs, dim=1)
        label = LABELS[idx.item()]
    return label, confidence.item()

