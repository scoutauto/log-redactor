# Log Redactor v0.1

Removes common secrets and personal data (API keys, tokens, emails, IP addresses) from log files before you share them in tickets, forums, or bug reports.

## Use

    python3 log-redact.py input.log > clean.log

- Standard library only, Python 3.8+, no network calls
- Tests included (8/8 passing)
- Patterns are plain regexes you can read and change

## Verify the download

    sha256sum -c SHA256SUMS

## Limits

This is a pattern-based filter, not a guarantee. Review the output before you publish it.

## Support

Free to use. Paid support or custom patterns on request.
