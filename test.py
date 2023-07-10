from flask import Flask

# Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다
app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello, {__name__}'

@app.route('/yeonji/')
def hello_yeonji():
    return f'Hello, yeonji'