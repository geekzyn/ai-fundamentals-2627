"""The models this project uses. Change them here."""

import ollama

# The language model. Ollama runs it on your own laptop: nothing you type or film leaves it.
#   16 GB of memory or more    "qwen3.5:4b"       3,3 GB download (the default)
#   8 GB of memory             "qwen3.5:2b"       2,7 GB download, clearly more mistakes
#   Apple silicon, 32 GB       "gemma4:12b-mlx"   7,7 GB download, slower and better
# After changing it, run  uv run python prepare.py  to download the new model.
CHAT_MODEL = "qwen3.5:4b"

# Ollama reserves memory for the longest conversation a model could have. This project
# never needs more than 8.192 tokens, and this keeps a 4b model near 4 GB instead of 8.
OLLAMA_OPTIONS = {"num_ctx": 8192}


def check_ollama(*models):
    """Stop with a clear message when Ollama is not running or a model is missing."""
    try:
        installed = {m.model for m in ollama.list().models}
    except ConnectionError:
        raise RuntimeError(
            "Ollama is not running. macOS: open the Ollama app. "
            "Linux and WSL: run  ollama serve  in a terminal and leave it open."
        ) from None
    missing = [m for m in models if m not in installed and f"{m}:latest" not in installed]
    if missing:
        raise RuntimeError("Missing model. Run  uv run python prepare.py  in a terminal, "
                           "then run the cell again. Missing: " + ", ".join(missing))
    print("Ollama is running, models ready:", ", ".join(models))
