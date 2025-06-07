import re

# Compiled regular expressions to match Markdown formatting.
_MARKDOWN_PATTERNS = [
    re.compile(r"\*\*(.*?)\*\*"),  # Bold
    re.compile(r"\*(.*?)\*"),  # Italic
    re.compile(r"_(.*?)_"),  # Underline
    re.compile(r"~~(.*?)~~"),                # Strikethrough
    re.compile(r"\[(.*?)\]\(.*?\)"),  # Links
    re.compile(r"!\[(.*?)\]\(.*?\)"),  # Images
    re.compile(r"`(.*?)`"),  # Inline code
    re.compile(r"^\s*#+\s*(.*?)\s*$", re.MULTILINE),  # Headers
]


def strip_markdown(text: str) -> str:
    """Remove Markdown formatting a given string.

    Removes Markdown syntax such as bold, italic, underline,
    strikethrough, links, images, inline code, and headers, returning
    only the plain text content.

    Args:
        text: The input string containing Markdown-formatted text.

    Returns:
        The plain text with Markdown formatting removed.

    Examples:
        >>> strip_markdown("**Bold** and *italic* text")
        'Bold and italic text'
    """
    for pattern in _MARKDOWN_PATTERNS:
        text = pattern.sub(r"\1", text)
    return text
