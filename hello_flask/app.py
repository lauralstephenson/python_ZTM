from flask import Flask
#this instantiates the app, and this file is __main__
app = Flask(__name__)

#this is a useful decorator
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"