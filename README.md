# Lecture # 5 - REST APIs with Flask

## Lecture Topics

- Building REST APIs with `flask-restful`
- Retrieve with `flask-restful` (handling `GET` requests)
- Create with `flask-restful` (handling `POST` requests)
- Update with `flask-restful` (handling `PATCH` requests)
- Delete with `flask-restful` (handling `DELETE` requests)

## Setup

1. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then enter the command `pipenv install` in your terminal to install the required packages.

2. Now that your `pipenv` virtual environment is ready to use, enter the command `pipenv shell` in your terminal to enter the virtual environment.

3. Enter the command `cd server` in your terminal to move into the server directory.

4. Run these two terminal commands while in the `server` directory:

```
export FLASK_APP=app.py

export FLASK_RUN_PORT=7777
```