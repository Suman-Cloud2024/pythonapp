from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(message="Running through Nork!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)