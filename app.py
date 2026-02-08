from flask import Flask, make_response
import os

# Get the directory where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    # Read file directly to avoid any caching issues
    with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        html = f.read()
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/debug')
def debug():
    # Show what files exist and first 500 chars of index.html
    files = os.listdir(BASE_DIR)
    with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        preview = f.read(500)
    return f"<pre>BASE_DIR: {BASE_DIR}\nFiles: {files}\n\nindex.html preview:\n{preview}</pre>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)