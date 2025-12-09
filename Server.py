from flask import Flask
import uuid

app = Flask(__name__)


@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        h1 {
            margin: 20px;
            padding: 20px;
            border-bottom: 2px solid #333;
        }
    </style>
</head>
<body>
    <h1>Home Page</h1>
</body>
</html>
"""

@app.route('/name')
def index():
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Welcome to the Server application !</h1>
</body>
</html>
"""

@app.route('/user/<username>')
def user(username):
    return f'<h1>My name is {username}!!</h1>'


@app.route('/calculate/addition/<int:a>/<int:b>')
def addition(a, b):
    result = a + b
    return f'<h1>{a} + {b} = {result}</h1>'

@app.route('/calculate/subtraction/<int:a>/<int:b>')
def subtraction(a, b):
    result = a - b
    return f'<h1>{a} - {b} = {result}</h1>'

@app.route('/calculate/multiplication/<int:a>/<int:b>')
def multiplication(a, b):
    result = a * b
    return f'<h1>{a} × {b} = {result}</h1>'

@app.route('/calculate/division/<int:a>/<int:b>')
def division(a, b):
    if b == 0:
        return '<h1>Error: Cannot divide by zero!</h1>', 400
    result = a / b
    return f'<h1>{a} ÷ {b} = {result:.2f}</h1>'


@app.route('/secretkey/<uuid:sk>')
def my_secretkey(sk):
    return f'<h1>Your secret key is {sk}</h1>'


if __name__ == '__main__':
    app.run(debug=True)