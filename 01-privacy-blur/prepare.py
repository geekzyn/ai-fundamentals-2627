"""Download and test what this project needs, once, so class time is not download time.

Run it inside this folder:

    uv run python prepare.py

It downloads about 100 MB of models. Running it again only checks what is there.
"""

import sys

print("Python", sys.version.split()[0])

# 1. The Python packages
missing = []
for module in ["cv2", "gradio", "huggingface_hub", "matplotlib", "torch", "transformers"]:
    try:
        __import__(module)
    except ImportError:
        missing.append(module)
if missing:
    sys.exit(f"Missing packages: {', '.join(missing)}\nRun:  uv pip install -r requirements.txt --torch-backend=cpu")
print("packages: all there")

# 2. The Hugging Face models
from huggingface_hub import hf_hub_download  # noqa: E402
from transformers import pipeline  # noqa: E402

print("hugging face: face detector")
hf_hub_download("opencv/face_detection_yunet", "face_detection_yunet_2023mar.onnx")
print("hugging face: object detector")
pipeline("object-detection", model="PekingU/rtdetr_v2_r18vd")

print("\nAll set. Open privacy_blur.ipynb in VS Code.")
