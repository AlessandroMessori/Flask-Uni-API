from flask import jsonify
from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()
parser.add_argument('category',required=True)
parser.add_argument('name',required=True)

class AllCourses(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self):
        data = self.helper.getData()
        data = sorted(data, key=lambda k: k['id'])
        return jsonify(data)

class Course(Resource):

    def __init__(self,helper):
        self.helper = helper

    def get(self,id):
        data = self.helper.getSingleData('id',id)
        return jsonify(data)

    def post(self,id):
        data = parser.parse_args()
        data['id'] = id
        try:   
            self.helper.addElement(data)
            return jsonify({'message':'OK'})
        except(e):
            print(e)
            return jsonify({'message':'error'})
        
    def put(self,id):
        data = parser.parse_args()
        data['id'] = id
        try:   
            self.helper.updateElement(data,'id',id)
            return jsonify({'message':'OK'})
        except(e):
            print(e)
            return jsonify({'message':'error'})

    def delete(self,id):
        try:   
            self.helper.deleteElement("id",id)
            return jsonify({'message':'deleted element with id '+str(id)})
        except:
            return jsonify({'message':'error'})
