# Log Redactor

A dependency-free Python tool that masks common secrets and PII in log text.

## What it redacts
- Email addresses -> `[REDACTED:email]`
- IPv4 addresses -> `[REDACTED:ip]`
- AWS access key IDs (AKIA/ASIA) -> `[REDACTED:aws_key]`
- JWTs -> `[REDACTED:jwt]`
- `Bearer` tokens -> `Bearer [REDACTED:token]`
- `password=`, `secret=`, `api_key=`, `token=` values -> `[REDACTED]`
- Card-like digit sequences -> `[REDACTED:card]`

## Usage
```
python3 redact.py input.log -o clean.log
cat app.log | python3 redact.py --stats
```

## Web demo (stdlib HTTP server)
```
python3 web_demo.py 8080
```
Then open http://127.0.0.1:8080, paste log lines, and submit.

## Tests
```
python3 test_redact.py
```

## Limits
Pattern-based, so it can miss unusual secret formats and can over-match some digit runs.
Review output before sharing logs publicly.
