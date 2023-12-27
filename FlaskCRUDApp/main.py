import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from sqlalchemy import Column, Integer, String, create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app)

engine = create_engine(os.environ.get('DATABASE_URL'))

# Create a declarative base for models
Base = declarative_base()

# Create a session class bound to the engine
Session = sessionmaker(bind=engine)


class Scientist(Base):

    __tablename__ = 'scientist'

    id = Column(Integer, primary_key=True)
    f_name = Column(String(100))
    country = Column(String(100))
    a_degree = Column(String(100))
    spec = Column(String(50))
    org = Column(String(100))


@app.route('/Scientist/', methods=['GET'])
def get_scientists():
    session = Session()
    return session.query(Scientist).all()



@app.route('/Scientist', methods=['POST'])
def create_scientist():
    if request.method == 'POST':
        data = request.json
        new_scientist = Scientist(name=data['name'], field=data['field'])
        Base.session.add(new_scientist)
        Base.session.commit()
        return jsonify({'message': 'Scientist created successfully'}), 201
    else:
        return jsonify({'message': 'Invalid request method'}), 405


@app.route('/Scientist/', methods=['PUT'])
def update_user(id_):
    if request.method == 'PUT':
        scientist = Scientist.query.get(id_)
        if scientist:
            data = request.json
            scientist.name = data.get('name', scientist.name)
            scientist.field = data.get('field', scientist.field)
            Base.session.commit()
            return jsonify({'message': f'Scientist {id_} updated successfully'}), 200
        else:
            return jsonify({'message': f'Scientist {id_} not found'}), 404
    else:
        return jsonify({'message': 'Invalid request method'}), 405


if __name__ == '__main__':
    app.run()
