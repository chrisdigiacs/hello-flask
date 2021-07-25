from flask import Flask, render_template

app =  Flask(__name__) 
#hello
#yo
#yoyoyoyo
@app.route("/")
def route_helloWorld():
    return render_template("hello.html")

@app.route("/<name>")
def route_hello_name(name):
    return "<h1>Hello, {name}!</h1>"