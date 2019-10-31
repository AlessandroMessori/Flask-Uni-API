import pymongo
from src.generator.generator import generateStudents

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["flask-uni-db"]

generateStudents(db,500)