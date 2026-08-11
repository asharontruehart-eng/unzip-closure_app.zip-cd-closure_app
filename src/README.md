This directory contains a minimal Python example for unzipping a closure_app.zip archive.

Files:
- main.py — small CLI with a safety check to prevent path traversal on extraction.

How to run:
1. (Optional) Create a virtualenv and install dependencies from requirements.txt.
2. Run:
   python src/main.py path/to/closure_app.zip --dest extracted_app

Notes:
- The example is intentionally minimal and safe for demonstration; extend it for your app's needs.
