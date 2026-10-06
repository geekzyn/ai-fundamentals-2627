# Profile check

**AI Fundamentals, Session 3, project 4 of 7**

A moderation check for profiles in English, Dutch and French: a word list, rules, a classifier and a language model.
Everything runs on your own laptop: no account, no API key, and nothing you type or film leaves your machine.

## Before the session, at home

You need the setup from the setup guide first: VS Code, uv and Git, and WSL on Windows.

**1. Install Ollama**, which runs language models on your laptop. You need it once, for projects 3 to 7.

- macOS: download it from [ollama.com/download](https://ollama.com/download), install it and open it once
- Linux, and Windows inside the Ubuntu terminal:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**2. Put this folder in your projects folder** and install what it needs:

```bash
cd ~/dev/04-profile-check
uv venv --python 3.14
uv pip install -r requirements.txt --torch-backend=cpu
```

`--torch-backend=cpu` installs the small version of PyTorch, without the gigabytes of graphics card drivers that nothing here needs.

**3. Download the models**, once:

```bash
uv run python prepare.py
```

This project needs the language model (3,3 GB by default) and a 540 MB classifier, plus 1 GB of packages. It ends with *All set* when everything works. Do this at home: on a shared network in class it takes far too long.

**4. Open the folder in VS Code** with `code .`, open `profile_check.ipynb`, select the `.venv` kernel at the top right and run the first cell.

## Which model for your laptop

The language model is set in `settings.py`. Pick it by your laptop's memory, then run `prepare.py` again.

| Memory | `CHAT_MODEL` | Download | |
| --- | --- | --- | --- |
| 8 GB | `qwen3.5:2b` | 2,7 GB | works, with clearly more mistakes |
| 16 GB or more | `qwen3.5:4b` | 3,3 GB | the default, used for the saved outputs |
| Apple silicon, 32 GB | `gemma4:12b-mlx` | 7,7 GB | slower, and better |

Ollama keeps one copy of each model for all projects, so the other projects reuse this download.

The saved outputs in the notebook come from a recent MacBook. On your laptop the answers can take several times longer, and with another model they will be worded differently.

## When something goes wrong

| Problem | Fix |
| --- | --- |
| *Ollama is not running* | macOS: open the Ollama app. Linux and WSL: run `ollama serve` in a second terminal and leave it open |
| *Missing model* | run `uv run python prepare.py` |
| The kernel dies, or everything is very slow | the model is too big for your memory: choose a smaller one in `settings.py` |
| *Cannot find the .venv kernel* | `uv pip install ipykernel`, then restart VS Code |
| Red text under a cell about `HF_TOKEN` or a progress bar | not an error: ignore it, you need no account |

## Sources

- [Multilingual toxicity classifier](https://huggingface.co/gravitee-io/distilbert-multilingual-toxicity-classifier), gravitee.io
- [Qwen 3.5](https://ollama.com/library/qwen3.5), language model, Alibaba
- The 37 profiles were written for this course and are fictional, including every name
