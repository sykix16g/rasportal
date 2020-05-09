# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.tpl.html")

if __name__ == "__main__":
   app.run(host='0.0.0.0')
