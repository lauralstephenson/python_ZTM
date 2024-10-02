from flask import Flask, render_template
#this instantiates the app, and this file is __main__
app = Flask(__name__)

#this is a useful decorator
@app.route("/")
def hello_world():
    #render_template looks into a template folder
    return render_template("index.html")

@app.route("/about.html")
def about():
    #render_template looks into a template folder
    return render_template("about.html")

@app.route("/blog") #this creates a new blog thread, so now there are 2 pages on the server
def blog():
    return "<p>These are my thoughts on blogs.</p>"

@app.route("/blog/2023/dogs") #now there are 3 pages on the server
def blog2():
    return "<p>This is my dog.</p>"