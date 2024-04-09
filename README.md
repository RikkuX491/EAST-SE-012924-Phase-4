# Lecture # 6 - Constraints and Validations

## Lecture Topics

- SQLAlchemy Constraints
  - `name = db.Column(db.String, nullable=False, unique=True)`
- CheckConstraint
  - `__table_args__ = (db.CheckConstraint('first_name != last_name'),)`
- Flask-SQLAlchemy Validations
  - `@validates('rating')`
  - ` @validates('first_name', 'last_name')`

## Setup

1. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then enter the command `pipenv install` in your terminal to install the required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter the command `pipenv shell` in your terminal to enter the virtual environment.

3. Enter the command `cd server` in your terminal to move into the server directory.

4. Run these two terminal commands while in the `server` directory:

```
export FLASK_APP=app.py

export FLASK_RUN_PORT=7777
```

5. Run `flask run --debug` or `python app.py` to run your flask app with Debug mode set to on.
