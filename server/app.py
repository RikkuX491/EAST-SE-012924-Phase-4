#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

# Deliverable 1
@app.route('/greeting/<first_name>/<last_name>')
def greeting(first_name, last_name):
    return f'<h1>Greetings, {first_name} {last_name}!</h1>'
    
# Deliverable 2
@app.route('/count_and_square/<int:number>')
def count_and_square(number):
    numbers_string = ""
    for n in range(1, number + 1):
        numbers_string += f'{n * n}\n'
    return numbers_string

if __name__ == "__main__":
    app.run(port=7777, debug=True)