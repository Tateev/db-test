from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app)
data = [
    {
        'user_id': 1,
        'name': 'value1',
        'surname': 'value2',
        'email': 'value3'
    },
    {
        'user_id': 2,
        'name': 'value2',
        'surname': 'value3',
        'email': 'value4'
    }
]


@app.route('/Users', methods=['GET'])
def get_users():
    return data


@app.route('/Users/<int:id_>', methods=['GET'])
def get_user(id_):
    for user in data:
        if user['user_id'] == id_:
            return user
    return {'error': 'User not found'}


@app.route('/Users', methods=['POST'])
def create_user():
    if 'name' in request.json and 'surname' in request.json and 'email' in request.json:
        new_user = {
            'user_id': len(data) + 1,
            'name': request.json['name'],
            'surname': request.json['surname'],
            'email': request.json['email']
        }
        data.append(new_user)
        return new_user


@app.route('/Users/<int:id_>', methods=['PUT'])
def update_user(id_):
    for user in data:
        if user['user_id'] == id_:
            user['name'] = request.json['name']
            user['surname'] = request.json['surname']
            user['email'] = request.json['email']
            return user
    return {'error': 'User not found'}


if __name__ == '__main__':
    app.run()
