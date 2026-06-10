from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

# Replace with your Gemini API key

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""

    if request.method == "POST":
        user_message = request.form["message"]

        chat_history.append(f"User: {user_message}")

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents="\n".join(chat_history)
            )

            response_text = response.text

            chat_history.append(f"Bot: {response_text}")

        except Exception as e:
            response_text = f"Error: {e}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)