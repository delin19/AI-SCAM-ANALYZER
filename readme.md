# AI Scam Analyzer

A Flask-based web application that uses Google's Gemini API to analyze messages for potential scam and phishing indicators.

## Features

- Analyze suspicious messages using AI
- Detect potential scam/phishing indicators
- Assign a risk level: High, Medium, or Low
- Explain the reasons behind the verdict
- Provide safety advice to the user
- Validate AI-generated responses before displaying them
- Secure API key handling using environment variables

## Tech Stack

- Python
- Flask
- Google Gemini API
- HTML
- CSS
- Jinja2
- Git & GitHub

## How It Works

1. The user enters a message into the web interface.
2. Flask receives the message through a POST request.
3. The message is sent to the Gemini API for analysis.
4. Gemini returns a structured JSON response.
5. The application validates the response.
6. The verdict, risk level, reasons, and advice are displayed to the user.
