import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>游竣程Python網頁</h1>"
    homepage += "<a href=/work>游竣程求職網頁</a><br>"

    return homepage


@app.route("/work")
def about():
    return render_template("16job.html")



#if __name__ == "__main__":
#app.run()