#!/usr/bin/env python3
"""Minimal web demo for the Log Redactor. Stdlib only.

Run: python3 web_demo.py [port]   (default port 8080)
GET  /  -> HTML form
POST /  -> form field 'log' is redacted and shown back
"""
import html
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

from redact import redact_line

PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>Log Redactor</title></head>
<body style="font-family:sans-serif;max-width:720px;margin:2em auto">
<h1>Log Redactor</h1>
<p>Paste log lines. Emails, IPs, AWS keys, JWTs, bearer tokens, key=value secrets and card numbers get masked.</p>
<form method="post" action="/">
<textarea name="log" rows="10" style="width:100%">{input}</textarea><br>
<button type="submit">Redact</button>
</form>
{output}
</body></html>"""


class Handler(BaseHTTPRequestHandler):
    def _send(self, body, status=200):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        self._send(PAGE.format(input="", output=""))

    def do_POST(self):
        length = min(int(self.headers.get("Content-Length", 0)), 100_000)
        form = parse_qs(self.rfile.read(length).decode("utf-8", errors="replace"))
        raw = form.get("log", [""])[0]
        clean = "".join(redact_line(l + "\n").rstrip("\n") + "\n" for l in raw.splitlines())
        output = f"<h2>Result</h2><pre>{html.escape(clean)}</pre>"
        self._send(PAGE.format(input=html.escape(raw), output=output))

    def log_message(self, fmt, *args):
        pass  # keep logs quiet


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    print(f"Serving on http://127.0.0.1:{port}")
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()
