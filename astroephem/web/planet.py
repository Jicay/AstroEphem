from flask_restful import Resource
from astroephem.services.ephemeride import *


class Planet(Resource):
    def get(self, name=None):
        if name is None:
            return 'All planets'
        else:
            return compute_planet(name)
        pass
