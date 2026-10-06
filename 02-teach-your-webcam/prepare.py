"""Download and test what this project needs, once, so class time is not download time.

Run it inside this folder:

    uv run python prepare.py

It downloads about 90 MB of models. Running it again only checks what is there.
"""

import sys

print("Python", sys.version.split()[0])

# 1. The Python packages
missing = []
for module in ["cv2", "gradio", "matplotlib", "sklearn", "torch", "transformers"]:
    try:
        __import__(module)
    except ImportError:
        missing.append(module)
if missing:
    sys.exit(f"Missing packages: {', '.join(missing)}\nRun:  uv pip install -r requirements.txt --torch-backend=cpu")
print("packages: all there")

# 2. The Hugging Face models
from transformers import AutoImageProcessor, AutoModel  # noqa: E402

print("hugging face: image features")
AutoImageProcessor.from_pretrained("facebook/dinov2-small")
AutoModel.from_pretrained("facebook/dinov2-small")

print("\nAll set. Open teach_your_webcam.ipynb in VS Code.")
