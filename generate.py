import pymongo
from src.generator.studentsGenerator import generateStudents
from src.generator.teachersGenerator import generateTeachers

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["flask-uni-db"]

generateStudents(db,500)
generateTeachers(db,30)