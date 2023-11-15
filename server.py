from flask import Flask, render_template, request
from datetime import datetime
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    
    homepage += "<a href=/about>游竣程求職網頁</a><br>"
    return homepage


serve(app, host='0.0.0.0', port=8080)
#if __name__ == "__main__":
#   app.run()