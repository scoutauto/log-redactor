import unittest

from redact import RULES, custom_rules, redact_line


class TestBuiltinRules(unittest.TestCase):
    def test_password_and_email_masked(self):
        out = redact_line("user=bob@example.com password=hunter2")
        self.assertNotIn("bob@example.com", out)
        self.assertNotIn("hunter2", out)

    def test_ip_masked(self):
        self.assertIn("[REDACTED:ip]", redact_line("from 10.0.0.5 ok"))

    def test_plain_text_untouched(self):
        self.assertEqual(redact_line("retry=3 status ok"), "retry=3 status ok")


class TestCustomPatterns(unittest.TestCase):
    def test_custom_hostname_and_customer_id(self):
        rules = RULES + custom_rules([r"db-prod-\d+\.internal", r"CUST-\d{6}"])
        out = redact_line("host db-prod-42.internal cust CUST-123456 ok", None, rules)
        self.assertNotIn("db-prod-42", out)
        self.assertNotIn("CUST-123456", out)
        self.assertEqual(out.count("[REDACTED:custom]"), 2)

    def test_no_custom_rules_leaves_hostname(self):
        out = redact_line("host db-prod-42.internal", None, RULES)
        self.assertIn("db-prod-42.internal", out)

    def test_invalid_regex_exits(self):
        with self.assertRaises(SystemExit):
            custom_rules(["("])


if __name__ == "__main__":
    unittest.main()
