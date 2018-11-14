from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.web.planet import Planet
from app.web.day import Day

app = Flask(__name__)
CORS(app)

api = Api(app)

api.add_resource(Planet, '/planets', '/planets/<name>', methods=['GET'])
api.add_resource(Day, '/days', methods=['GET'])


@app.route('/')
def hello_world():
    return 'Hello World!'
