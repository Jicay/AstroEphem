from flask_restful import Resource


class Planet(Resource):
    def get(self, name=None):
        if name is None:
            return 'All planets'
        else:
            return name
        pass
