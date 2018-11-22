from flask import Flask
from flask_restful import Api

from app.web.planet import Planet
from app.web.day import Day
from app.web.location import Location

app = Flask(__name__)
api = Api(app)

api.add_resource(Planet, '/planets', '/planets/<name>', methods=['GET'])
api.add_resource(Day, '/days', methods=['GET'])
api.add_resource(Location, '/locations', methods=['GET'])


@app.route('/')
def hello_world():
    return 'Hello World!'