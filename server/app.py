#!/usr/bin/env python3
import ipdb

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hotel, Customer

app = Flask(__name__)

# configure a database connection to the local file examples.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

@app.route('/hotels')
def all_hotels():
    hotels = Hotel.query.all()
    hotel_list_with_dictionaries = [hotel.to_dict() for hotel in hotels]
    return make_response(hotel_list_with_dictionaries)

if __name__ == "__main__":
    app.run(port=7777, debug=True)