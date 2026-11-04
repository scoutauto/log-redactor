# Log Redactor (free CLI, MIT)

Strip secrets and personal data from log files before you paste them into a bug report, support ticket, or public issue.

- Redacts emails, IPv4 addresses, AWS access key IDs, JWTs, bearer tokens, password/token/api_key values, and card-like numbers.
- No dependencies. Python 3 standard library only.
- CLI: `python3 redact.py app.log -o clean.log` or pipe with `--stats` to see counts.
- Local web form: `python3 web_demo.py 8080`.
- Tests: `python3 test_redact.py` (8 passing).

Limits: pattern-based. It can miss unusual secret formats and can over-match some digit runs. Review output before sharing.

Feedback and pattern requests are welcome.
