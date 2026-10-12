
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser
import threading
import os

HOST = "127.0.0.1"
PORT = 8000

# Find the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

# Check whether the original HTML file exists
if not (BASE_DIR / "index.html").exists():
    print("ERROR: index.html file not found!")
    print("Place app.py and index.html in the same folder.")
    raise SystemExit(1)

# Start the local web server
server = ThreadingHTTPServer(
    (HOST, PORT),
    SimpleHTTPRequestHandler
)

url = f"http://{HOST}:{PORT}/index.html"

print("EarGuardian dashboard is running!")
print(f"Open this URL: {url}")
print("Press Ctrl+C to stop the server.")

# Open the dashboard in your browser
threading.Timer(
    1,
    lambda: webbrowser.open(url)
).start()

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nEarGuardian server stopped.")
finally:
    server.server_close()
