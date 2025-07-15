from flask import Flask, request, render_template, jsonify
from chatbot import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not request.is_json:
        return jsonify({"error": "Invalid request: JSON expected"}), 400

    data = request.get_json()
    input_text = data.get("message", "").strip()

    if not input_text:
        return jsonify({"error": "Missing input text"}), 400

    try:
        response = generate_response(input_text)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5050, debug=True)
