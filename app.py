from flask import Flask,request,json
from flask_smorest import abort

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)