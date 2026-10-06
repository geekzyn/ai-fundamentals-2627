# Privacy blur

**AI Fundamentals, Session 3, project 1 of 7**

A live face blur for your webcam, then a people counter for a room.
Everything runs on your own laptop: no account, no API key, and nothing you type or film leaves your machine.

## Before the session, at home

You need the setup from the setup guide first: VS Code, uv and Git, and WSL on Windows.

**1. Put this folder in your projects folder** and install what it needs:

```bash
cd ~/dev/01-privacy-blur
uv venv --python 3.14
uv pip install -r requirements.txt --torch-backend=cpu
```

`--torch-backend=cpu` installs the small version of PyTorch, without the gigabytes of graphics card drivers that nothing here needs.

**2. Download the models**, once:

```bash
uv run python prepare.py
```

This project needs about 100 MB of models, plus 1 GB of packages. It ends with *All set* when everything works. Do this at home: on a shared network in class it takes far too long.

**3. Open the folder in VS Code** with `code .`, open `privacy_blur.ipynb`, select the `.venv` kernel at the top right and run the first cell.

The saved outputs in the notebook come from a recent MacBook. On your laptop the answers can take several times longer.

## The webcam

The apps open as a page in your browser, which asks for permission to use the camera: allow it. For live video, press **Record** under the webcam image; for a single picture, press the camera button.

- **Windows with WSL:** this works, because the browser on Windows uses the camera and sends the images to the notebook in Ubuntu
- **Nothing is published.** The page runs on your own laptop at an address starting with `127.0.0.1`, which nobody else can reach
- If the page does not open by itself, click the link under the cell

## When something goes wrong

| Problem | Fix |
| --- | --- |
| The camera stays black | allow the camera for this page in your browser, and close other apps that use it (Teams, Zoom) |
| *Cannot find the .venv kernel* | `uv pip install ipykernel`, then restart VS Code |
| Red text under a cell about `HF_TOKEN` or a progress bar | not an error: ignore it, you need no account |

## Sources

- [YuNet](https://huggingface.co/opencv/face_detection_yunet), face detection, OpenCV
- [RT-DETR v2](https://huggingface.co/PekingU/rtdetr_v2_r18vd), object detection
- Expedition 64 crew portrait, NASA, public domain
- Coffee photo by Rachel Michetti, CC0, from the scikit-image sample data
