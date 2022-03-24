import os
from flask import Flask, escape, request,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from src.helpers.helpers import DataHelper
from src.resources.teachers import AllTeachers,Teacher,TeachersByDep
from src.resources.students import AllStudents,Student
from src.resources.courses import AllCourses,Course
from src.resources.auth import Register,Login


app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(app)
db = mongo.db["flask-uni-db"]

# Sets up JWT authentication
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


# Helpers to load the data from the db
usersHelper = DataHelper("Users",db)
studentsHelper = DataHelper("Students",db)
teachersHelper = DataHelper("Teachers",db)
coursesHelper = DataHelper("Courses",db)

@app.route('/')
def home():
  return "<h2>Welcome to Flask Uni API</h2>"

# exposes all the API Endpoints

api.add_resource(Register, '/register',
                 resource_class_kwargs={'helper': usersHelper})
api.add_resource(Login, '/login',
                 resource_class_kwargs={'helper': usersHelper})
api.add_resource(AllTeachers, '/teachers',
                 resource_class_kwargs={'helper': teachersHelper})
api.add_resource(Teacher, '/teachers/<int:id>',
                 resource_class_kwargs={'helper': teachersHelper})
api.add_resource(TeachersByDep, '/teachersByDep/<string:dep>',
                 resource_class_kwargs={'helper': teachersHelper})
api.add_resource(AllStudents, '/students',
                 resource_class_kwargs={'helper': studentsHelper})
api.add_resource(Student, '/students/<int:id>',
                 resource_class_kwargs={'helper': studentsHelper})
api.add_resource(AllCourses, '/courses',
                 resource_class_kwargs={'helper': coursesHelper})
api.add_resource(Course, '/courses/<int:id>',
                 resource_class_kwargs={'helper': coursesHelper})


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
