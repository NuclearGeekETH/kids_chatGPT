import os
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai_key = os.environ["openai_key"]
openai.api_key = openai_key
conversation_history = []

# Set initial system message
system_message = "You are a chat assistant for a 6-year-old genius child. You are to provide him with answers to his questions along with guidance and detailed information on the subject he is requesting."

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/chat', methods=["POST"])
def chat():
    global conversation_history
    user_message = request.form.get('user_message', '')

    conversation_history.append({"role": "system", "content": system_message})
    conversation_history.append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )
    result = response["choices"][0]["message"]["content"]

    conversation_history.append({"role": "assistant", "content": result})
    conversation_history = conversation_history[-3:]  # Keep only the last three messages to avoid exceeding the token limit

    return jsonify({"response": result.strip()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7863, debug=True)