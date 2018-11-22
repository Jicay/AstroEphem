import os

from flask_restful import Resource, reqparse
import requests


class Location(Resource):
    def get(self):
        MAP_KEY = os.environ['MAP_KEY']
        parser = reqparse.RequestParser()
        parser.add_argument('query', required=True, help="Query cannot be blank!")
        args = parser.parse_args()

        query = args['query']

        url = 'https://geocoder.tilehosting.com/q/' + query + '.js?key=' + MAP_KEY
        response = requests.get(url)
        return response.json()
