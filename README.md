# Lecture # 2 - Flask-SQLAlchemy

## Lecture Topics

- Flask-SQLAlchemy
- Database Migration
  - `flask db migrate`
- Flask Shell
- Querying a Database in a Flask Application
  - `Hotel.query.all()`
  - `Hotel.query.first()`
  - `Hotel.query.filter(Hotel.id == 1).first()`
  - `Hotel.query.filter_by(id = 1).first()`
  - `db.session.get(Hotel, 1)`
- Seeding a Database
- Serialization
- Returning a JSON response
- Other important Flask db terminal commands
- `flask db init`
- `flask db upgrade`
- `flask db downgrade`
- Adding new rows to the database, and committing to save changes
  - `db.session.add(hotel1)`
  - `db.session.commit()`
- Deleting rows from a table
  - `db.session.delete(hotel1)`
  - `Hotel.query.delete()`

## Setup

1. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then enter the command `pipenv install` in your terminal to install the required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter the command `pipenv shell` in your terminal to enter the virtual environment.

3. Enter the command `cd server` in your terminal to move into the server directory.

4. Run these two terminal commands while in the `server` directory:

```
export FLASK_APP=app.py

export FLASK_RUN_PORT=7777
```