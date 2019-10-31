import numpy as np
import names
import random 
import pymongo
from ..resources.resource import Resource

def getMat(dbCon):
 prev = dbCon["Students"].find().sort('mat',-1).limit(1)
 
 if (prev.count() == 0):
     return 880000
 
 return int(prev[0]['mat'])+1

def checkLimit(num):
    if (num > 30.00):
         return 30.00
    if (num < 18.00):   
         return 18.00
    return num

def getGrade():
    gpa = round(np.random.normal(24,2),2)
    return checkLimit(gpa)

def getExams(courses):
    
    predictedGpa = getGrade()
    sum  = 0 
    for course in courses:
        grade = checkLimit(int(np.random.normal(predictedGpa,0.5)))
        course["grade"] = grade
        sum += grade 

    gpa = round(sum/len(courses),2)
    gpa = checkLimit(gpa)
    return (courses, gpa)

def generateStudents(dbCon,dim):

    courses = list(Resource("Courses",dbCon).getData())

    for i in range(0,dim):
        
        gender = "male" if (random.choice([True, False]))  else "female"
        exams,gpa = getExams(courses)

        currentStudent = {
            "mat":getMat(dbCon),
            "name":names.get_first_name(gender=gender),
            "surname":names.get_last_name(),
            "gpa": gpa,
            "gender":gender,
            "exams":exams
        }

        dbCon["Students"].insert_one(currentStudent)

