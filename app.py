from flask import Flask, render_template
from functools import reduce
from itertools import chain
from data import tours, departures

app = Flask(__name__)


@app.route('/')
def render_main():
    prepared_tours = reduce(
        lambda prev, t: prev + [dict(chain.from_iterable(d.items() for d in ({'id': t[0]}, t[1])))], tours.items(),
        [])
    print(prepared_tours)
    return render_template('index.html', prepared_tours=prepared_tours)


@app.route('/departures/<departure>/')
def render_departures(departure):
    departure_display_name = departures[departure]
    return render_template('departure.html', departure_display_name=departure_display_name)


@app.route('/tours/<id>')
def render_tour(id):
    return render_template('departure.html', id=id)


app.run(debug=True)
