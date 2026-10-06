"""Download and test what this project needs, once, so class time is not download time.

Run it inside this folder:

    uv run python prepare.py

It downloads the language model (3,3 GB by default) and a 540 MB classifier. Running it again only checks what is there.
"""

import sys

print("Python", sys.version.split()[0])

# 1. The Python packages
missing = []
for module in ["gradio", "ollama", "pandas", "pydantic", "torch", "transformers"]:
    try:
        __import__(module)
    except ImportError:
        missing.append(module)
if missing:
    sys.exit(f"Missing packages: {', '.join(missing)}\nRun:  uv pip install -r requirements.txt --torch-backend=cpu")
print("packages: all there")

# 2. The Ollama models
import ollama  # noqa: E402

from settings import CHAT_MODEL, OLLAMA_OPTIONS  # noqa: E402

try:
    installed = {m.model for m in ollama.list().models}
except ConnectionError:
    sys.exit("Ollama is not running. macOS: open the Ollama app. "
             "Linux and WSL: run  ollama serve  in another terminal, then run this again.")

for model in [CHAT_MODEL]:
    if model in installed or f"{model}:latest" in installed:
        print(f"ollama {model}: already there")
        continue
    print(f"ollama {model}: downloading")
    shown = -10
    for progress in ollama.pull(model, stream=True):
        if progress.total and progress.completed:
            percent = 100 * progress.completed / progress.total
            if percent >= shown + 10:            # one line every 10%
                shown = percent
                print(f"   {percent:3.0f}% of {progress.total / 1e9:.1f} GB")
    print(f"ollama {model}: done")

# 3. The Hugging Face models
from transformers import pipeline  # noqa: E402

print("hugging face: toxicity classifier")
pipeline("text-classification", model="gravitee-io/distilbert-multilingual-toxicity-classifier")

# 4. One real answer
import time  # noqa: E402

start = time.time()
answer = ollama.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": "Reply with the word ready."}],
                     options=OLLAMA_OPTIONS, think=False).message.content
print(f"{CHAT_MODEL} says {answer.strip()!r} in {time.time() - start:.1f} s")

print("\nAll set. Open profile_check.ipynb in VS Code.")
