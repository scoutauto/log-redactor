# Log Redactor v0.1 - Quickstart

Removes secrets and personal data from log files before you share them.

## Use

    python3 log-redact.py input.log > clean.log

Standard library only. Python 3.8+. No network calls.

## Verify the download

    sha256sum -c SHA256SUMS

## What it catches

Check the script for the full list of patterns. Each pattern is a plain regex you can read and change.

## Limits

- It is a pattern-based filter. Review the output before you publish it.
- It does not parse structured formats. Treat JSON logs as plain text.
