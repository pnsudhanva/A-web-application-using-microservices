from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts."
]

@app.route('/joke', methods=['GET'])
def get_joke():
    joke = random.choice(jokes)
    return jsonify({'joke': joke})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
