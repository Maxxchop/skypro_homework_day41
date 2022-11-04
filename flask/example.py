from flask import Flask
import random
# Это уже знакомое callable WSGI-приложение
app = Flask(__name__)

@app.get('/')
def hello_get():
    return 'Hello, GET!'

@app.post('/')
def hello_post():
    return 'Hello, POST!'

@app.get('/users')
def users_get():
    return 'GET /users'

@app.post('/users')
def users():
    return 'Users', 302

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'