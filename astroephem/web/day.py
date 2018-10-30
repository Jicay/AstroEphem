from flask_restful import Resource
from astroephem.services.ephemeride import *


class Day(Resource):
    def get(self):
        return get_current_days()
        pass
