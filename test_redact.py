import unittest
from redact import redact_line


class RedactTests(unittest.TestCase):
    def test_email(self):
        self.assertEqual(redact_line("user bob@example.com logged in"),
                         "user [REDACTED:email] logged in")

    def test_ipv4(self):
        self.assertIn("[REDACTED:ip]", redact_line("from 192.168.1.20 port 22"))

    def test_aws_key(self):
        self.assertIn("[REDACTED:aws_key]", redact_line("key=AKIAIOSFODNN7EXAMPLE"))

    def test_jwt(self):
        tok = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.abcdefghijk"
        self.assertIn("[REDACTED:jwt]", redact_line(f"auth {tok}"))

    def test_bearer(self):
        self.assertIn("Bearer [REDACTED:token]", redact_line("Authorization: Bearer abcdef123456"))

    def test_kv_secret(self):
        self.assertEqual(redact_line("password=hunter2"), "password=[REDACTED]")

    def test_card(self):
        self.assertIn("[REDACTED:card]", redact_line("card 4111 1111 1111 1111 ok"))

    def test_clean_line_untouched(self):
        line = "INFO request completed in 42ms\n"
        self.assertEqual(redact_line(line), line)


if __name__ == "__main__":
    unittest.main()
