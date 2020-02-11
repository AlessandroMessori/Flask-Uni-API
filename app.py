import os
from flask import Flask, escape, request,jsonify
from flask_restful import Api
import pymongo
from src.helpers.helpers import DataHelper
from src.resources.teachers import AllTeachers,Teacher,TeachersByDep
from src.resources.students import AllStudents,Student
from src.resources.courses import AllCourses,Course

#client = pymongo.MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["flask-uni-db"]

studentsHelper = DataHelper("Students",db)
teachersHelper = DataHelper("Teachers",db)
coursesHelper = DataHelper("Courses",db)

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
  #returns the welcome message
  return "<h2>Welcome to Flask Uni API</h2>"


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
    app.run(host="0.0.0.0")

