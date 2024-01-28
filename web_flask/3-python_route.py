#!/usr/bin/python3
"""
    App start point with flask
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def what_is_c(text):
    """ displays c <text> """
    new_text = text.replace("_", " ")
    return "c {}".format(new_text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"})
def what_is_python(text):
    """ displays Python <text> """
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
