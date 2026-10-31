# Log Redactor: offer

**What it is:** A small, dependency-free Python tool that masks secrets and personal data in log files before they are shared (support tickets, bug reports, public issue trackers).

**Redacts:** email addresses, IPv4 addresses, AWS access key IDs, JWTs, bearer tokens, password/secret/api_key/token values, and card-like numbers.

**How to use:**
- CLI: `python3 redact.py app.log -o clean.log` or `cat app.log | python3 redact.py --stats`
- Local web form: `python3 web_demo.py 8080`, then paste logs in the browser.

**Verification:** 8 unit tests pass (`python3 test_redact.py`).

**Limits (stated honestly):** pattern-based, so it can miss unusual secret formats and can over-match some digit runs. Review output before publishing logs.

**Status:** working prototype, free to use. No payment or account has been set up. Any offer of payment would need the creator's approval.
