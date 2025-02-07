#!/usr/bin/python3
"""9. Cities by states"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """ """
    storage.close()


@app.route("/cities_by_states")
def states_list():
    """List of all State objects by cities present in DBStorage"""
    st = storage.all(State)
    return render_template('8-cities_by_states.html', states=st)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
