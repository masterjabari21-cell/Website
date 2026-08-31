#!/usr/bin/env python3
"""Local dev server for the personal website.

Usage:
    python3 serve.py            # serves on http://localhost:8000
    python3 serve.py 5500       # serves on http://localhost:5500

Serves the current directory with no-cache headers so edits show up on
refresh, and opens the site in your default browser.
"""

import http.server
import socketserver
import sys
import webbrowser
from functools import partial
from pathlib import Path

ROOT = Path(__file__).parent.resolve()


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))


def main():
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            sys.exit("Port must be a number, got: %r" % sys.argv[1])

    handler = partial(Handler, directory=str(ROOT))

    with socketserver.TCPServer(("", port), handler) as httpd:
        url = "http://localhost:%d/" % port
        print("Serving %s" % ROOT)
        print("  -> %s  (Ctrl+C to stop)" % url)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
