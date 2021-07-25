from flask import Flask, render_template

app =  Flask(__name__) 
#hello
#yo
#yoyoyoyo
@app.route("/")
def helloWorld():
    return render_template("hello.html")

