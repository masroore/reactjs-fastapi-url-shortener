import secrets
import string

from w3lib.url import canonicalize_url


def normalize_url(url: str) -> str:
    return canonicalize_url(url)


def generate_random_id(max_len: int = 5) -> str:
    return "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(max_len)
    )
