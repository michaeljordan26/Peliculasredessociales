from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Bienvenido a Peliculasredessociales API'})

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    keyword = data.get('keyword', '')
    return jsonify({'results': f'Publicaciones para {keyword}'})

if __name__ == '__main__':
    app.run(debug=True)