from flask import Flask, render_template
from markupsafe import escape

app =  Flask(__name__) 
#hello
#yo
#yoyoyoyo

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/projects")
def projects_page():
    return render_template("projects.html")

@app.route("/<name>")
def route_hello_name(name):
    return f"Hello, {escape(name)}!"