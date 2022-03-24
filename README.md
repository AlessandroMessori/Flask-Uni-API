# Flask-Uni-API


## Introduction
This is a side project that I made during my universty years in order to get familiar with a set of skills and technologies I was feeling was missing from my toolbox at the time. 
It consists of an REST API that exposes fictional university data, alongside the code to generate and plot such data.

## Technologies Used
 - Python
 - Flask
 - Docker
 - MongoDB

## Endpoints
 - /register 
    - POST
 - /login
    - POST
 - /teachers    
    - GET
 - /teachers/:id
    - GET, POST, PUT, DELETE 
 - /students
    - GET
 - /students/:id
    - GET, POST, PUT, DELETE 
 - /courses
    - GET 
 - /courses/:id
    - GET, POST, PUT, DELETE 



## Scripts
 - app.py --> starts up the backend server to serve the requests
 - generate.py --> Generates realistic collections of students and teachers and loads them in the Mong datastore
 - analyze.py --> Plots the distribution of the student's GPA and of the distribution of teachers by department 
