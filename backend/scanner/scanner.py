"""Small, public-web-only security header scanner using the Python standard library."""

from datetime import datetime, timezone
import http.client
import ipaddress
import socket
import ssl
from urllib.parse import urljoin, urlsplit, urlunsplit

from .checks.headers import check_security_headers


class ScanError(ValueError):
    """A target cannot be scanned safely or could not be reached."""


def validate_url(url):
    if not isinstance(url, str) or any(ord(char) <= 32 or ord(char) == 127 for char in url):
        raise ScanError("Enter a complete HTTP or HTTPS URL without spaces or control characters.")
    try:
        parts = urlsplit(url)
        if parts.scheme not in ("http", "https") or not parts.hostname:
            raise ValueError()
        if parts.username is not None or parts.password is not None or "\\" in url:
            raise ValueError()
        host = parts.hostname.encode("idna").decode("ascii")
        if "%" in host:
            raise ValueError()
        port = parts.port or (443 if parts.scheme == "https" else 80)
        if port not in (80, 443):
            raise ValueError()
    except (ValueError, UnicodeError) as exc:
        raise ScanError("Use an HTTP or HTTPS URL on port 80 or 443, without credentials.") from exc
    return parts, host, port