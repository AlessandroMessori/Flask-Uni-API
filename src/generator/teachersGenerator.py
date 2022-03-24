import numpy as np
import names
import random 
import pymongo
from ..helpers.helpers import DataHelper

departments = ['mat','ele','inf','fis','bio']

def getId(dbCon):
 prev = dbCon["Teachers"].find().sort('id',-1).limit(1)

 if (prev.count() == 0):
     return 0
 
 return int(prev[0]['id'])+1

# generates the teachers data assigning a random department and generating random the personal data with a random name generator
def generateTeachers(dbCon,dim):

    for i in range(0,dim):
        
        gender = "male" if (random.choice([True, False]))  else "female"
        ran  = random.randint(0,len(departments)-1)

        currentTeacher = {
            "id":getId(dbCon),
            "name":names.get_first_name(gender=gender),
            "surname":names.get_last_name(),
            "department":  departments[ran],
            "gender":gender,
        }

        dbCon["Teachers"].insert_one(currentTeacher)
