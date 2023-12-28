#!/usr/bin/python3
"""4. Is it a number?"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """print hello"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """Display C followed by the value of the text"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def py(text):
    """Display Python followed by the value of the text"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def number(n):
    """Display “n is a number” only if n is an integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
