from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from math_solver import solve_math
from voice_input import get_voice_input

import os
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

FOUNDER_REPLY = (
    "I was created by Jayson, Krushna, Sadhwik, and Gagenesh of 6 Tulip."
)

def is_founder_question(text):
    keys = ["founder", "inventor", "creator", "maker", "who made you"]
    return any(k in text.lower() for k in keys)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]

    if is_founder_question(user):
        return jsonify(reply=FOUNDER_REPLY)

    math_result = solve_math(user)
    if math_result is not None:
        return jsonify(reply=f"Answer: {math_result}")

    response = model.generate_content(user)
    return jsonify(reply=response.text)

@app.route("/voice", methods=["POST"])
def voice():
    text = get_voice_input()
    return jsonify(message=text)

if __name__ == "__main__":
    app.run(debug=True)

