#!/usr/bin/env python3
"""Log Redactor: masks common secrets and PII in log text.

Usage:
  python3 redact.py < input.log > output.log
  python3 redact.py input.log -o clean.log
  python3 redact.py --stats input.log
"""
import argparse
import re
import sys

# (name, pattern, replacement)
RULES = [
    ("aws_access_key", re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b"), "[REDACTED:aws_key]"),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{5,}\b"), "[REDACTED:jwt]"),
    ("bearer", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/=-]{8,}"), "Bearer [REDACTED:token]"),
    ("kv_secret", re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key|token)(\s*[=:]\s*)(\S+)"),
     r"\1\2[REDACTED]"),
    ("email", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[REDACTED:email]"),
    ("ipv4", re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b"),
     "[REDACTED:ip]"),
    ("credit_card", re.compile(r"\b(?:\d[ -]?){13,16}\b"), "[REDACTED:card]"),
]


def redact_line(line, counts=None):
    for name, pattern, repl in RULES:
        new, n = pattern.subn(repl, line)
        if n and counts is not None:
            counts[name] = counts.get(name, 0) + n
        line = new
    return line


def redact_stream(lines, counts=None):
    for line in lines:
        yield redact_line(line, counts)


def main(argv=None):
    p = argparse.ArgumentParser(description="Redact secrets and PII from logs.")
    p.add_argument("input", nargs="?", help="input file (default: stdin)")
    p.add_argument("-o", "--output", help="output file (default: stdout)")
    p.add_argument("--stats", action="store_true", help="print redaction counts to stderr")
    args = p.parse_args(argv)

    src = open(args.input, encoding="utf-8", errors="replace") if args.input else sys.stdin
    counts = {} if args.stats else None
    out = open(args.output, "w", encoding="utf-8") if args.output else sys.stdout
    try:
        for line in redact_stream(src, counts):
            out.write(line)
    finally:
        if src is not sys.stdin:
            src.close()
        if out is not sys.stdout:
            out.close()
    if counts is not None:
        total = sum(counts.values())
        print(f"redacted {total} items: {counts}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
