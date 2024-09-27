from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    # 텍스트를 처리하는 로직을 추가할 수 있습니다.
    return jsonify({"message": f"Received: {text}"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
