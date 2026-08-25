from flask import Flask, render_template, request
from main import analyze_message,validation
import os


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze",methods=["POST"])
def analyze_route():
    message=request.form["message"]
    if not message.strip():
        return render_template(
            "index.html",
            error="Please enter a message to analyze."
        )
    if len(message) > 5000:
        return render_template(
            "index.html",
            error="Message is too long. Please enter a message under 5000 characters."
        )

    try:
        result = analyze_message(message)

    except Exception as e:
        print("Analysis error:", e)

        return render_template(
            "index.html",
            error="Unable to contact the AI service. Please try again later."
        )

    if not validation(result):
        return render_template(
            "index.html",
            error="Unable to analyze the message. Please try again."
        )

    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
