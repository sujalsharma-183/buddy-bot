from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv # <-- 1. Import the helper library
import os

# 2. Automatically load hidden variables from your .env file
load_dotenv() 

app = Flask(__name__)

# This will now successfully find your API key from the .env file!
client = genai.Client()

# ... (rest of your chat route code remains the same!)
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Hardcoding the key here skips the terminal setup entirely!
# Change this line
client = genai.Client()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    try:
        # Call the Gemini 2.5 Flash model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
        )
        return jsonify({"reply": response.text})
        
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)