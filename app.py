{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96eb28f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "from textblob import TextBlob\n",
    "\n",
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "from flask import render_template,request\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        text = request.form.get(\"text\")\n",
    "        print(text)\n",
    "        r = TextBlob(text).sentiment\n",
    "        return(render_template(\"index.html\", result=r))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"waiting...\"))\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4c2a04d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
