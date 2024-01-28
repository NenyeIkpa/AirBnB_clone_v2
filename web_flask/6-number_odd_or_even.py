"""
    App start point with flask
"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def is_a_number(n):
    """ displays n if int """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """ displays n as an html tag if int """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    num_type = "even" if n % 2 == 0 else "odd"
    return render_template(
            "6-number_odd_or_even.html",
            num=n,
            num_type=num_type
            )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
