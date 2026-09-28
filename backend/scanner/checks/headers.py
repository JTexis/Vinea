SECURITY_HEADERS = {
    "Content-Security-Policy": {
        "severity": "Medium",
        "description": "Content Security Policy is not configured.",
        "recommendation": "Configure a Content-Security-Policy header."
    },
    "Strict-Transport-Security": {
        "severity": "Medium",
        "description": "HTTP Strict Transport Security is not configured.",
        "recommendation": "Configure the Strict-Transport-Security header."
    },
    "X-Content-Type-Options": {
        "severity": "Low",
        "description": "X-Content-Type-Options is not configured.",
        "recommendation": "Set X-Content-Type-Options to nosniff."
    },
    "X-Frame-Options": {
        "severity": "Medium",
        "description": "X-Frame-Options is not configured.",
        "recommendation": "Configure X-Frame-Options or an appropriate CSP frame-ancestors policy."
    },
    "Referrer-Policy": {
        "severity": "Low",
        "description": "Referrer-Policy is not configured.",
        "recommendation": "Configure an appropriate Referrer-Policy."
    },
    "Permissions-Policy": {
        "severity": "Low",
        "description": "Permissions-Policy is not configured.",
        "recommendation": "Configure Permissions-Policy according to the application's needs."
    }
}


def check_security_headers(headers):
    findings = []

    for header, info in SECURITY_HEADERS.items():
        if header not in headers:
            findings.append({
                "type": "missing_security_header",
                "name": header,
                "severity": info["severity"],
                "description": info["description"],
                "recommendation": info["recommendation"]
            })

    return findings