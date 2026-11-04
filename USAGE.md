# log-redactor: usage

Removes secrets and personal data from log files before you share them.

    python3 log-redact.py input.log > clean.log

What it redacts:
- API keys and bearer tokens
- Email addresses
- IPv4 addresses
- Common password=/secret= key-value pairs

Run it on a copy. Review the output before sharing. It is a pattern-based tool and can miss secrets that don't match its patterns.

Example:

    echo 'user=bob@example.com token=abc123 ip=10.0.0.5' | python3 log-redact.py -
