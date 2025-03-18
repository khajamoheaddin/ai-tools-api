from flask import Blueprint, request, jsonify
import requests
import os

# Create a Blueprint for the grammar checker tool
grammar_checker_bp = Blueprint('grammar_checker', __name__)

# Deepseek R1 LLM API endpoint
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/grammar_check"

# API key for Deepseek R1 LLM (store securely in environment variables)
DEEPSEEK_API_KEY = os.getenv("sk-352c361f073447e480b6f69d812a7229")

@grammar_checker_bp.route("/check_grammar", methods=["POST"])
def check_grammar():
    """
    Endpoint to handle grammar checking requests.
    """
    data = request.json
    text = data.get("text")
    tone = data.get("tone", "neutral")  # Default tone is neutral
    language = data.get("language", "en")  # Default language is English

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Customize the prompt sent to the LLM here.
    prompt = f"""
    Analyze the following text for grammar, spelling, punctuation, and style errors. 
    Provide detailed corrections and explanations for each error. 
    Adjust the tone to be {tone} and ensure the language is {language}.
    Return the corrected text along with confidence scores for each suggestion.
    Text: {text}
    """

    # Send the prompt to the Deepseek R1 LLM
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": prompt,  # The customized prompt
        "text": text,  # The original text
        "tone": tone,  # Tone adjustment
        "language": language,  # Language support
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500