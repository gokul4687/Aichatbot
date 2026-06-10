from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat_history = []

print("🤖 Gemini Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break

    chat_history.append(f"User: {user_input}")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="\n".join(chat_history)
        )

        bot_response = response.text

        print("Bot:", bot_response)

        chat_history.append(f"Bot: {bot_response}")

    except Exception as e:
        print("Error:", e)