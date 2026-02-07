# AI-Powered CV Analysis Using Gemini AI (gemini-3-flash-preview)

This project analyzes CVs using Gemini AI and categorizes experience into different job domains.

## Quickstart

```bash
# 1) Build the image
docker build -t cv_analyzer .

# 2) Run the app (interactive)
docker run -it --name cv_analyzer_app cv_analyzer
```

## Features
- Extracts text from PDF and DOCX CVs
- Categorizes experience into domains (e.g., AI, Business, Marketing)
- Suggests job roles based on experience
- Provides improvement recommendations
