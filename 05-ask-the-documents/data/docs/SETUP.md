# Setup a Python development environment

The basics to get you started with Python, on Windows, macOS or Linux.

## Contents

Set up, once

1. [How this works](#1-how-this-works), what you install and why
2. [Your platform](#2-your-platform), and why Windows means WSL
3. [Install VS Code](#3-install-vs-code)
4. [Install uv](#4-install-uv)
5. [Set up Git](#5-set-up-git), your project folder and `.gitignore` included
6. [Verify your setup](#6-verify-your-setup), proof that the steps above worked

Every project

7. [Open and run a project](#7-open-and-run-a-project), the commands you repeat
8. [Notebooks](#8-notebooks)
9. [Adding packages](#9-adding-packages)
10. [API keys](#10-api-keys), and how to avoid leaking one

11. [Official documentation](#11-official-documentation)

---

# Set up, once

## 1. How this works

You install three tools, in this order. You do not install Python yourself, because
uv fetches it for you the first time you create an environment.

| Tool | What it does |
| --- | --- |
| VS Code | Editor, terminal and notebook viewer in one window |
| uv | Installs Python, creates environments, manages packages |
| Git | Records the history of your work, so you can go back |

Each project is a folder, and each one gets its own `.venv`:

```
~/dev/
├── first-project/
│   └── .venv/     this project's Python and packages
├── second-project/
│   └── .venv/     a completely separate set
└── third-project/
    └── .venv/
```

`.venv` is the only thing you need to understand. It is a private copy of Python
plus the packages one project needs, sitting in that project's folder. Because
every project has its own, a package you install for one cannot break another.

Two commands manage it, and you will use them constantly:

- `uv venv --python 3.14` builds the `.venv` for the project you are in
- `uv run` runs something inside it

You do not install Python separately. `uv venv --python 3.14` fetches that version
the first time it needs it, and reuses it afterwards. Pick a version and stay on
it across your projects, so an error you hit is one someone else can reproduce.

## 2. Your platform

| Your machine | What to do |
| --- | --- |
| macOS | Follow the macOS blocks throughout |
| Linux | Follow the Linux blocks throughout |
| Windows | Do [section 2.1](#21-windows-install-wsl-first) first, then follow the Linux blocks throughout |

### 2.1 Windows: install WSL first

WSL (Windows Subsystem for Linux) runs a real Ubuntu inside Windows. In this
guide, every Windows user works in WSL.

This is not about Windows being inferior. Most Python tooling, documentation and
deployment targets assume Linux. Working in WSL means the commands you read online
are the commands you run, and what works on your laptop works on a server.

#### Requirements

- Windows 11, or Windows 10 version 2004 and higher, build 19041 and higher
- Administrator rights on the machine
- Hardware virtualisation enabled in the firmware, which is the default on nearly all machines bought in the last decade

If any of those fails, the installer says so clearly, and you will have to work
natively on Windows instead.

#### Install

Open **PowerShell as administrator**, right-click PowerShell and choose
**Run as administrator**, then:

```powershell
wsl --install
```

This enables the required Windows components, installs the Linux kernel, sets
WSL 2 as the default and installs Ubuntu.

**Restart your machine** when it asks.

#### First launch

After the restart, open Ubuntu from the Start menu. It asks you to create a
Linux username and password.

- These are separate from your Windows account, and unrelated to it
- While you type the password, **nothing appears on screen**. That is normal, keep typing and press Enter
- This account can run `sudo`, so keep the password somewhere you will find it again

Then bring the system up to date:

```bash
sudo apt update && sudo apt upgrade
```

Confirm it worked, back in PowerShell:

```powershell
wsl --list --verbose
```

You want to see `Ubuntu`, state `Running` or `Stopped`, and version 2.

#### Three rules that prevent almost every WSL problem

1. Keep your files in the Linux filesystem. Work in `~/dev/ai-fundamentals` inside Ubuntu, never in `/mnt/c/Users/...`. Microsoft is explicit that working across the two filesystems slows things down significantly. To reach your Linux files from Windows Explorer, use `\\wsl$\Ubuntu\home\<your-username>`, or run `explorer.exe .` from inside WSL
2. Install uv inside Ubuntu. uv installed on Windows is a different program and cannot see your Linux environments. If you already installed it on Windows, install it again inside Ubuntu
3. Install VS Code on Windows, not inside Ubuntu. VS Code stays a Windows application and connects into WSL. Section 3 covers this

#### Where you type things from now on

Everything in this guide goes in the Ubuntu terminal, not PowerShell, unless a
command is explicitly marked PowerShell. Follow the Linux blocks for every
remaining step.

## 3. Install VS Code

Download it from [code.visualstudio.com/download](https://code.visualstudio.com/download), pick the build for your
system and run the installer.

Windows and WSL: install the normal Windows build. Do not install VS Code
inside Ubuntu. Tick **Add to PATH** during installation.

macOS: take the .dmg that matches your distribution.

Linux: take the .deb or .rpm that matches your distribution.

### 3.1 Extensions

Open VS Code, press `Ctrl+Shift+X` (`Cmd+Shift+X` on macOS) and install:

- WSL by Microsoft, Windows user only, marketplace id `ms-vscode-remote.remote-wsl`
- Python by Microsoft
- Jupyter by Microsoft
- Ruff by Astral, our formatter and linter

Windows user: install the WSL extension first, then open a WSL window
before installing the other three, so they land inside Ubuntu where your code runs.
Section 7 shows how.

## 4. Install uv

macOS, Linux, and Windows inside the Ubuntu terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> Now close every terminal window and open a new one. The installer adds uv to
> your PATH, and only new terminals read it. Skipping this produces the single most
> common error in this guide.

Check it:

```bash
uv --version
```

You should see a version number. If you see "command not found", you skipped the
step above: close every terminal window, open a new one and try again.

Already a Homebrew user on macOS? `brew install uv` works just as well.

## 5. Set up Git

Git records the history of a project on your own machine.
### 5.1 Install it

Windows in Ubuntu, and Linux:

```bash
sudo apt install git
```

macOS: run `git --version`. If Git is missing, macOS offers to install the
developer tools. Accept, and let it finish.

Check it either way:

```bash
git --version
```

### 5.2 Tell Git who you are

Every change you record carries a name and an email. Set them once:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Use an address you intend to keep. If you later put work on GitHub, use the same
one there, otherwise your changes will not show up as yours.

### 5.3 Create a project folder

One folder per project, tracked by Git from the start.

```bash
mkdir -p ~/dev/my-project
cd ~/dev/my-project
code .
git init
```

Windows users: type this in the Ubuntu terminal, so the folder lands in the
Linux filesystem rather than on the Windows side.

Where this folder sits matters more than it looks:

| Your machine | Use | Avoid |
| --- | --- | --- |
| Windows with WSL | `~/dev` inside Ubuntu | Anything under `/mnt/c/` |
| macOS | `~/dev` | iCloud Drive, or Desktop with iCloud on |
| Linux | `~/dev` | Any Dropbox or Drive folder |

### 5.4 Keep secrets and clutter out, with .gitignore

Two things must never end up in Git:

- `.env` files, and anything else holding an API key
- `.venv` folders, which are rebuilt in seconds and which would add thousands of files

`.gitignore` is a plain text file listing what Git should pretend it cannot see.
Write it now, before your first commit, in the folder you just created:

```bash
cat > .gitignore <<'EOF'
# Python environments
.venv/
__pycache__/
*.py[cod]

# Secrets, never commit these
.env
*.key

# Notebooks
.ipynb_checkpoints/

# Editors and operating systems
.vscode/
.idea/
.DS_Store
Thumbs.db
EOF
```

Or make it in VS Code: right-click in the Explorer panel on the left, choose
New File, and name it `.gitignore`, with the leading dot and no extension. Then
paste the lines between `cat` and `EOF` above.

Two things to know about it:

- Check it works with `git status`. Neither `.env` nor `.venv/` should appear in the list
- The rules only apply to files Git is not already tracking. If you committed a `.env` before writing the rule, Git carries on tracking it. Stop it with `git rm --cached .env`, then commit again

### 5.5 The loop you repeat

Inside the folder Git is tracking:

```bash
git status                      # what have I changed
git diff                        # show me the actual changes
git add .                       # stage everything I changed
git commit -m "what I did"      # record it
git log --oneline               # what happened so far
```

Commit whenever something works. A commit is a save point you can return to, and
small frequent ones are far more useful than one enormous commit at the end.

VS Code shows the same information in its Source Control panel on the left-hand
bar. Use whichever you prefer, they are the same underneath.

## 6. Verify your setup

This builds a throwaway environment and checks every piece you just installed.
It needs nothing else.

```bash
mkdir -p ~/dev/check-setup
cd ~/dev/check-setup
uv venv --python 3.14
uv pip install numpy pandas
uv run python -c "import sys, numpy, pandas; print('python', sys.version.split()[0]); print('env   ', sys.prefix); print('numpy ', numpy.__version__); print('pandas', pandas.__version__)"
```

Windows users: type this in the Ubuntu terminal, not PowerShell.

---

# Every project

## 7. Open and run a project

> The rule: open the project folder itself, never a folder above it.
> One project, one VS Code window. This single habit prevents most
> "it cannot find my packages" problems.

```bash
cd ~/dev/my-project
uv venv --python 3.14        # first time in this folder only
uv pip install numpy pandas  # whatever the project needs
code .
uv run python main.py
```

After the first time, the `.venv` is already there. Opening the folder and running
`uv run python main.py` is all you need.

Windows users: run `code .` from the Ubuntu terminal, never from
PowerShell. VS Code opens on Windows and connects into Ubuntu. Check the
bottom-left corner of the window reads **WSL: Ubuntu**. The first run downloads a
small server component into Ubuntu, which takes a moment once and never again.

VS Code detects `.venv` and asks whether to use it. Say yes. To check or change it
later: `Ctrl+Shift+P`, then **Python: Select Interpreter**, then the entry ending in
`.venv`. Open the built-in terminal with `` Ctrl+` ``, which gives you a shell
already inside the project folder.

Three habits:

- Always `uv run python`, never plain `python`
- Always `uv pip install`, never bare `pip install`
- One `.venv` per project folder, never one shared between projects

`uv run` guarantees the command uses that project's environment whether or not
anything is activated. That is why this guide skips activation scripts entirely.

## 8. Notebooks

Open any `.ipynb` file, click **Select Kernel** at the top right, choose
**Python Environments**, then the entry ending in `.venv`.

No `.venv` in the list means the project lacks the kernel package:

```bash
uv pip install ipykernel
```

Restart VS Code and it appears. If you prefer JupyterLab in a browser:

```bash
uv run --with jupyter jupyter lab
```

WSL users: the link it prints opens in your Windows browser as normal.

## 9. Adding packages

Inside the project folder, with its `.venv` already created:

```bash
uv pip install scikit-learn       # add a package to this project
uv pip uninstall scikit-learn     # remove it
uv pip list                       # see what is installed
```

This touches only the `.venv` in the folder you are standing in. No other
project, and no other Python on your machine, is affected.

If you want to record what a project needs, so you can rebuild it later or hand
it to someone else:

```bash
uv pip freeze > requirements.txt          # write the list
uv pip install -r requirements.txt        # rebuild from the list
```

## 10. API keys

Many projects need an API key, for a model provider or any other service. Keys are
personal and must never reach the repository.

1. Create a file called `.env` in the project folder
2. Paste your key after the `=`, with no quotes and no spaces
3. Read it in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

Check that `.env` is in your `.gitignore`, see [section 5.4](#54-keep-secrets-and-clutter-out-with-gitignore).
Without that line, your key travels with your code the first time you push it anywhere.

> Never paste a key into a notebook cell, a screenshot or a chat message. If you
> leak one, revoke it on the provider's website immediately. Deleting the file is
> not enough, because it is already in your git history.

## 11. Official documentation

- [uv installation](https://docs.astral.sh/uv/getting-started/installation/), Astral
- [uv documentation](https://docs.astral.sh/uv/), Astral
- [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install), Microsoft Learn
- [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment), Microsoft Learn
- [Basic commands for WSL](https://learn.microsoft.com/en-us/windows/wsl/basic-commands), Microsoft Learn
- [Troubleshooting WSL](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting), Microsoft Learn
- [Developing in WSL](https://code.visualstudio.com/docs/remote/wsl), Visual Studio Code
- [Download VS Code](https://code.visualstudio.com/download), Microsoft

