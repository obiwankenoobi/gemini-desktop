#!/usr/bin/env python3
"""
Simple HTTP server to preview the landing page locally
"""
import http.server
import socketserver
import webbrowser
import os
import sys

# Change to landing page directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def serve_landing_page():
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🌐 Serving landing page at http://localhost:{PORT}")
            print(f"📁 Directory: {os.getcwd()}")
            print("📝 Opening in browser...")
            print("⌨️  Press Ctrl+C to stop the server")
            
            # Open in browser
            webbrowser.open(f'http://localhost:{PORT}')
            
            # Start server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n✅ Server stopped")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use. Try a different port.")
            sys.exit(1)
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)

if __name__ == "__main__":
    serve_landing_page()