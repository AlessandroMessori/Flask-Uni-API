import requests
import numpy as np
import matplotlib.pyplot as plt
import json

data =  requests.get("http://127.0.0.1:5000/students")
data = json.loads(data.content)

gpas = [int(stud["gpa"]) for stud in data]

plt.hist(gpas)
plt.show()