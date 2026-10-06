"""An MCP server that gives any AI application access to the notes in data/notes.

The notebook 06_tools_and_mcp.ipynb starts it. Other applications can start it too:
give them this project's Python as the command and this file as the argument.
"""

import datetime
from pathlib import Path

from mcp.server.mcpserver import MCPServer
from mcp_types import ToolAnnotations

NOTES = Path(__file__).parent / "data" / "notes"
server = MCPServer("notes")

# Each tool is an ordinary Python function with one decorator. The docstring and the type
# hints become the description the language model reads. The annotations tell the
# application which tools only look (readOnlyHint) and which can destroy (destructiveHint),
# so it knows when to ask the user first.


@server.tool(annotations=ToolAnnotations(readOnlyHint=True))
def today() -> str:
    """Today's date and day of the week."""
    return datetime.date.today().strftime("%A %d %B %Y")


@server.tool(annotations=ToolAnnotations(readOnlyHint=True))
def list_notes() -> str:
    """The titles of all notes, one per line."""
    return "\n".join(sorted(p.stem for p in NOTES.glob("*.md")))


@server.tool(annotations=ToolAnnotations(readOnlyHint=True))
def read_note(title: str) -> str:
    """Read one note.

    Args:
        title: the title of the note, exactly as list_notes gives it
    """
    path = NOTES / f"{title}.md"
    return path.read_text(encoding="utf-8") if path.exists() else f"There is no note called {title!r}."


@server.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False))
def save_note(title: str, text: str) -> str:
    """Save a note. A note with the same title is replaced.

    Args:
        title: the title of the note
        text: the full text of the note, in Markdown
    """
    (NOTES / f"{title}.md").write_text(text, encoding="utf-8")
    return f"Saved the note {title!r}."


@server.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True))
def delete_note(title: str) -> str:
    """Delete a note permanently.

    Args:
        title: the title of the note to delete
    """
    path = NOTES / f"{title}.md"
    if not path.exists():
        return f"There is no note called {title!r}."
    path.unlink()
    return f"Deleted the note {title!r}."


if __name__ == "__main__":
    server.run()   # talk to the application over standard input and output
