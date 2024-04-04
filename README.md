# Lecture # 3 - Modeling Relationships in Flask-SQLAlchemy

## Lecture Topics

- One-To-Many Relationships with Flask-SQLAlchemy
  - `reviews = db.relationship('Review', back_populates='hotel')`
  - `hotel = db.relationship('Hotel', back_populates='reviews')`
- Cascades
  - `reviews = db.relationship('Review', back_populates='hotel', cascade='all')`
- Setting up Foreign Key columns in a table
  - `hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))`
- Many-To-Many Relationships with Flask-SQLAlchemy
- Association Proxy
  - `customers = association_proxy('reviews', 'customer', creator = lambda c: Review(customer = c))`
- Serialization with Relationships
  - `rules=('-reviews.hotel', '-reviews.customer')`
  - `only=('id', 'name')`
  - `serialize_rules`
  - `serialize_only`

## Setup

1. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then enter the command `pipenv install` in your terminal to install the required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter the command `pipenv shell` in your terminal to enter the virtual environment.

3. Enter the command `cd server` in your terminal to move into the server directory.

4. Run these two terminal commands while in the `server` directory:

```
export FLASK_APP=app.py

export FLASK_RUN_PORT=7777
```