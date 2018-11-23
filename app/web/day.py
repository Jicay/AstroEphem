from flask_restful import Resource, reqparse
from app.services.ephemeride import *


class Day(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lon', type=float)
        parser.add_argument('lat', type=float)
        parser.add_argument('timezone', type=int)
        args = parser.parse_args()

        lat = args['lat']
        lon = args['lon']
        zone = args['timezone']

        if lat is None:
            lat = 0

        if lon is None:
            lon = 0

        if zone is None:
            zone = 0

        return get_current_days(lat, lon, zone)
        pass
