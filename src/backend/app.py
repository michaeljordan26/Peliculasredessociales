from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Bienvenido a Peliculasredessociales API'})

if __name__ == '__main__':
    app.run(debug=True)