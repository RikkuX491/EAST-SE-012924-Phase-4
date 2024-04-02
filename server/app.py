#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my website!</h1>'

@app.route('/another_page')
def different_page():
    return '<h1>This is another page!</h1>'

@app.route('/intro/<name>')
def intro(name):
    return f"<h1>Hi! My name is {name}.</h1>"

@app.route('/intro/<name>/<int:age>')
def hello(name, age):
    # print(f'Name is a {type(name)}')
    # age = float(age)
    # print(f'Age is a {type(age)}')
    return f"<h1>Hi! My name is {name}. I'm {age} years old!</h1>"

@app.route('/<float:number>')
def float_example(number):
    return f"<h1>The number is {number}</h1>"

@app.route('/greeting/<first_name>/<last_name>')
def greeting(first_name, last_name):
    return f'<h1>Greetings, {first_name} {last_name}!</h1>'
    
@app.route('/count_and_square/<int:number>')
def count_and_square(number):
    numbers_string = ""
    for n in range(1, number + 1):
        numbers_string += f'{n * n}\n'
    return numbers_string

if __name__ == "__main__":
    app.run(port=7777, debug=True)