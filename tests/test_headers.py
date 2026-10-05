import unittest

from backend.scanner.checks.headers import check_security_headers

class securityHeadersTestCase(unittest.TestCase):
    def test_no_headers_return_six_findings(self):
        # Arrange: simulate a response with no headers
        headers = {}

        # Act: run the function we want to test
        findings = check_security_headers(headers)  

        # Assert: check the number and names of the reported headers
        self.assertEqual(len(findings), 6)
        self.assertCountEqual(
            [finding["name"] for finding in findings],
            [
                "Content-Security-Policy",
                "Strict-Transport-Security",
                "X-Content-Type-Options",
                "X-Frame-Options",
                "Referrer-Policy",
                "Permissions-Policy"
            ],
        )

    def test_some_headers_present_header_returns_five_findings(self):
        headers = {"X-Content-Type-Options": "nosniff"}

        findings = check_security_headers(headers)

        self.assertEqual(len(findings), 5)
        self.assertNotIn(
            "X-Content-Type-Options",
            [finding["name"] for finding in findings]
            )

    def test_all_headers_present_returns_no_findings(self):
        
        # These are sample inputs, not a policy recommendation for every site.
        headers = {
        "Content-Security-Policy": "default-src 'self'",
        "Strict-Transport-Security": "max-age=31536000",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Permissions-Policy": "camera=(), microphone=()"
        }

        findings = check_security_headers(headers)

        self.assertEqual(findings, [])

if __name__ == "__main__":
    unittest.main()

    



