#!/usr/bin/env python3

from app import app
from models import db, Example, Hotel, Customer

with app.app_context():
    Example.query.delete()
    Hotel.query.delete()
    Customer.query.delete()

    example1 = Example(columnname="Greetings", price=4.99, age=34)
    example2 = Example(columnname="Good day", price=34.78, age=56)
    example3 = Example(columnname="swimming", price=23.87, age=23)

    hotel1 = Hotel(name="Marriott")
    hotel2 = Hotel(name="Hampton Inn")
    hotel3 = Hotel(name="The Chanler at Cliff Walk")

    customer1 = Customer(first_name="Alice", last_name="Baker")
    customer2 = Customer(first_name="Bob", last_name="Willis")
    customer3 = Customer(first_name="Cindy", last_name="Davidson")
    
    db.session.add_all([example1, example2, example3])
    db.session.add_all([hotel1, hotel2, hotel3])
    db.session.add_all([customer1, customer2, customer3])
    # db.session.add(example2)
    # db.session.add(example3)

    db.session.commit()
    # Write code to seed hotels into the hotels table in the database
    print("🌱 Examples, Hotels, and Customers successfully seeded! 🌱")