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
        text = request.form.get("text")
        print(text)
        r1 = TextBlob(text).sentiment
        r2 = classifier(text)
        return(render_template("index.html", result1=r1, result2=r2))
    else:
        return(render_template("index.html", result1="2", result2="2"))

if __name__=="__main__":
    app.run()

