import os
from google import genai
import json

api_key = os.getenv("GEMINI_API_KEY")


def analyze_message(message):
    print("API KEY FOUND:", api_key is not None)
    client = genai.Client(api_key=api_key)
    try:


        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""
       Analyze the following message for scam or phishing indicators.

You MUST return valid JSON with exactly these four fields:

{{
    "verdict": "Scam" | "Safe" | "Suspicious",
    "risk": "High" | "Medium" | "Low",
    "reasons": ["reason 1", "reason 2", "reason 3"],
    "advice": ["advice 1", "advice 2", "advice 3"]
}}

Rules:

1. verdict MUST be exactly one of:
   - "Scam"
   - "Safe"
   - "Suspicious"

2. risk MUST be exactly one of:
   - "High"
   - "Medium"
   - "Low"

3. reasons MUST be a JSON array of separate strings.

4. advice MUST be a JSON array of separate strings.

5. Even if the message is meaningless, random, or unclear, DO NOT return an error.
   Analyze it and use "Suspicious" or "Low" when there is not enough evidence
   to classify it as clearly safe or a scam.

Message:
        {message}
        """,
            config=genai.types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )

        result = json.loads(response.text)

        return result


    except Exception as e:
        print("ERROR TYPE:", type(e))
        print("ERROR:", e)
        raise e


def display_results(result):

    print("Verdict: ",result["verdict"])
    print("Risk: ",result["risk"])
    print("\nReasons")
    for reason in result["reasons"]:
        print("-",reason)

    print("\nAdvice: ")
    for advice in result["advice"]:
        print("-",advice)

def validation(result):
    if result is None:
        return False

    if "verdict" not in result:
       return False


    if "risk" not in result:
        return False

    if not isinstance(result["reasons"], list):
        return False

    if not isinstance(result["advice"], list):
        return False

    if result["verdict"] not in ["Scam", "Safe", "Suspicious"]:
        return False

    if result["risk"] not in ["High", "Medium", "Low"]:
        return False


    return True







