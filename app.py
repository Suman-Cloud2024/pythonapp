from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(message="This is Suman Anantha - Welcome to my Flask application! END to END application completed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)