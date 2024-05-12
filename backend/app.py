from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/api/data', methods=['GET'])
@cross_origin()
def get_data():
    data = {'message': 'Hello from Jeb!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)