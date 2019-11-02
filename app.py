from flask import Flask, escape, request
import pymongo
import json
from src.resources.resource import Resource

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["flask-uni-db"]

studentsRes = Resource("Students",db)
teachersRes = Resource("Teachers",db)
coursesRes = Resource("Courses",db)

app = Flask(__name__)

@app.route('/')
def home():
  #returns the welcome message
  return "<h1> Welcome to the Flask Uni API </h1>"


@app.route('/students')
def allStudents():
  #returns the welcome message
  data  = studentsRes.getData()
  return json.dumps(data)

@app.route('/students/<int:id>')
def students(id):
  #returns the welcome message
  data = studentsRes.getSingleData("mat",id)
  return json.dumps(data)


@app.route('/courses')
def allCourses():
  #returns the welcome message
  data = coursesRes.getData()
  data = sorted(data, key=lambda k: k['id'])
  return json.dumps(data)

@app.route('/courses/<int:id>')
def courses(id):
  #returns the welcome message
  data = coursesRes.getSingleData('id',id)
  return json.dumps(data)

@app.route('/teachers')
def allTeachers():
  #returns the welcome message
  data = teachersRes.getData()
  data = sorted(data, key=lambda k: k['id'])
  return json.dumps(data)

@app.route('/teachers/<int:id>')
def teachers(id):
  #returns the welcome message
  data = teachersRes.getSingleData('id',id)
  return json.dumps(data)

@app.route('/teachersByDep/<string:dep>')
def teachersByDep(dep):
  #returns the welcome message
  data = teachersRes.getFilteredData('department',dep)
  return json.dumps(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
