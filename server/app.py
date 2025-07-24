# server/app.py

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from mistralai import Mistral, models
from mistralai.models import ChatCompletionResponse

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise RuntimeError("📌 Please set MISTRAL_API_KEY in .env")

client = Mistral(api_key=api_key)

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    body = request.json
    messages = body.get("messages")
    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    try:
        response: ChatCompletionResponse = client.chat.complete(
            model="mistral-small-latest",
            messages=messages,
            stream=False
        )
        return jsonify(response.dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
