#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from textblob import TextBlob

from flask import Flask

app = Flask(__name__)

from flask import render_template,request

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return(render_template("index.html", result="temp"))
    else:
        return(render_template("index.html", result="waiting..."))

if __name__=="__main__":
    app.run()

