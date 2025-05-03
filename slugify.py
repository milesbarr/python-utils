import re
import unicodedata


def slugify(s: str) -> str:
    """
    Convert a string into a URL-friendly slug.

    This function transforms the input string to lower case,
    transliterates to ASCII, removes all characters except alphanumeric
    and hyphens, and replaces spaces and contiguous groups of spaces
    with a single hyphen.

    Args:
        s (str): The string to be slugified.

    Returns:
        str: The slugified version of the input string.

    Examples:
        slugify("Hello World!") returns "hello-world"
        slugify("Python@# 3.8") returns "python-38"
    """
    slug = s.lower()
    slug = (
        unicodedata.normalize("NFKD", slug)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug
