import os
import pymongo
import json
from src.generator.studentsGenerator import generateStudents
from src.generator.teachersGenerator import generateTeachers

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
#client = pymongo.MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
db = client["flask-uni-db"]

with open("courses.json") as json_file:
    data = json.load(json_file)
    db["Courses"].insert_many(data)


generateStudents(db,50)
generateTeachers(db,10)
