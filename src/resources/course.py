from .resource import Resource

class Course(Resource):
    def __init__(self, name, con):
        super().__init__(name, con)
    