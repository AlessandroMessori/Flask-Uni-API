import requests
import numpy as np
import matplotlib.pyplot as plt
import json

s_data =  requests.get("http://127.0.0.1:5000/students")
s_data = json.loads(s_data.content)

t_data =  requests.get("http://127.0.0.1:5000/teachers")
t_data = json.loads(t_data.content)

gpas = [int(stud["gpa"]) for stud in s_data]
deps = [dep["department"] for dep in t_data]

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(gpas)
ax1.set_title("Students GPA Distribution")
ax2.hist(deps)
ax2.set_title("Teachers Departments Distribution")


plt.show()