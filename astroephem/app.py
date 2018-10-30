from flask import Flask
from flask_restful import Api

from astroephem.web.planet import Planet
from astroephem.web.day import Day

app = Flask(__name__)
api = Api(app)

api.add_resource(Planet, '/planets', '/planets/<name>', methods=['GET'])
api.add_resource(Day, '/days', methods=['GET'])


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
