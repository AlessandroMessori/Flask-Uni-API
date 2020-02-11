from flask import jsonify
from flask_restful import Resource,reqparse
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256 as sha256

parser = reqparse.RequestParser()
parser.add_argument('username',required=True)
parser.add_argument('password',required=True)

class Register(Resource):
 
    def __init__(self,helper):
        self.helper = helper

    def post(self):
        data = parser.parse_args()
        data['password'] = sha256.hash(data['password'])

        user = self.helper.getFilteredData('username',data['username'])

        if (len(user) > 0):
            return {'message':'this user already exists'}

        try:
            self.helper.addElement(data)
            return {'token':create_access_token(identity=user)}
        except:
            return {'message':'error'}


class Login(Resource):
 
    def __init__(self,helper):
        self.helper = helper

    def post(self):
        data = parser.parse_args()

        user = self.helper.getFilteredData('username',data['username'])

        if (len(user) == 0):
            return {'message':'this user does not exists'}
        elif sha256.verify(data['password'],user[0]['password']):
            return {'token':create_access_token(identity=user[0])}
        else:
            return {'message':'wrong password'}

  