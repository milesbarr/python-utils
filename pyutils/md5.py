import re

_MD5_RE = re.compile(r"^[a-f0-9]{32}$")


def is_md5(s: str) -> bool:
    """Check if a string is a valid MD5 hash.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a valid MD5 hash, False otherwise.
    """
    return bool(_MD5_RE.match(s))
