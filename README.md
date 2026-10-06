# AI Fundamentals, Session 3 projects

Seven small projects about computer vision and language models. Each one is a notebook
that explains every step and ends in a small app you can use. Everything runs on your own
laptop: no account, no API key, and nothing you film or type leaves your machine.

**Every project is its own folder**, with its own README, its own `.venv` and its own
`prepare.py` that downloads only what that project needs. Do them in any order, and only
the ones you want.

| Folder | You build | It shows | Webcam | Download |
| --- | --- | --- | --- | --- |
| [01-privacy-blur](01-privacy-blur) | a live face blur, then a people counter for a room | detection, thresholds, detection versus recognition | yes | 0,1 GB |
| [02-teach-your-webcam](02-teach-your-webcam) | your own image classifier, trained on 30 examples per class | transfer learning, and what a model really learns | yes | 0,1 GB |
| [03-read-it-for-me](03-read-it-for-me) | receipts and business cards to data, descriptions for someone who cannot see | vision language models, structured output, invented answers | yes | 3,3 GB |
| [04-profile-check](04-profile-check) | a moderation check for profiles in English, Dutch and French | rules against classifiers against language models, a person in the loop | no | 3,9 GB |
| [05-ask-the-documents](05-ask-the-documents) | a helpdesk that answers from a guide, with sources | embeddings, retrieval-augmented generation (RAG), testing | no | 3,9 GB |
| [06-tools-and-mcp](06-tools-and-mcp) | a study assistant that reads and writes your notes | tools, the agent loop, MCP, prompt injection | no | 3,3 GB |
| [07-a-team-of-agents](07-a-team-of-agents) | a cover letter writer that is checked by a reviewer | multi-agent systems, and when they are worth it | no | 3,3 GB |

The download column is the models, on top of the Python packages. Projects 3 to 7 share
one language model: Ollama keeps a single copy, so after the first of them, the others
only add what is new (0,6 GB for project 4's classifier, 0,6 GB for project 5's
embedding model).

## How to run one project

You need the setup from the setup guide first: VS Code, uv and Git, and WSL on Windows.
Then, for the project you want, open its README and follow the four steps there. In short:

```bash
cd ~/dev/01-privacy-blur
uv venv --python 3.14
uv pip install -r requirements.txt --torch-backend=cpu
uv run python prepare.py
code .
```

Projects 3 to 7 also need Ollama, once: the README of each of them says how.

Each project takes 15 to 25 minutes in class. Run `prepare.py` at home: on a shared
network the downloads take far too long.
