from flask import Flask, request, url_for, redirect, session, flash, render_template
from functools import wraps
app = Flask(__name__)
app.secret_key = 'do you even lift'

@app.route("/")
def homepage():
    return render_template ("home.html")

@app.route("/about")
def about():
   return render_template("about.html")
@app.route("/weeknd")
def weeknd():
    return render_template("weeknd.html")

@app.route("/ed")
def ed():
    return render_template("ed.html")
	
@app.route("/bob")
def bob():
    return render_template("bob.html")

@app.route("/logic")
def logic():
    return render_template("logic.html")

@app.route("/james")
def james():
    return render_template("james.html")

@app.route("/ferre")
def ferre():
    return render_template("ferre.html")

@app.route("/kendrick")
def kendrick():
    return render_template("kendrick.html")

@app.route("/miguel")
def miguel():
    return render_template("miguel.html")

@app.route("/logout")
def out():
   session.pop('logged_out', None)
   if ("logout" != None):
       flash ("You are now logged out")
   return redirect (url_for('login')) 

@app.route("/cat")
def cat():
    return render_template("cat.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form ["username"] != "chris" or request.form ["password"] != "chris":
            error = "Wrong password or username. Please try again."
        else:
          session['logged_in']=True
          return redirect (url_for("cat"))
    return render_template("login.html", error=error)

if __name__== "__main__":
    app.run(host='0.0.0.0', debug=True)


