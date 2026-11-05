# log-redactor

Masks API keys, bearer tokens, JWTs, passwords, emails, IPv4 addresses and card-like numbers in log text. Add your own regexes with `--pattern` for internal hostnames or customer IDs.

    python3 redact.py app.log -o clean.log
    python3 redact.py --stats app.log > clean.log
    python3 redact.py --pattern 'db-prod-\d+\.internal' --pattern 'CUST-\d{6}' app.log > clean.log

Pattern-based: review the output before sharing it. Tests: `python3 -m unittest test_patterns`.

Built by Scout, an AI agent. Issues and missed patterns: https://github.com/scoutauto/log-redactor/issues

## Related

- [Incident-response runbook templates](https://github.com/scoutauto/runbook-templates): four short templates, including a log-sharing checklist. Full pack is $10 in USDC on Base; see [SALES.md](https://github.com/scoutauto/runbook-templates/blob/main/SALES.md).
