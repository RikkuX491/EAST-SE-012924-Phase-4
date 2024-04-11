# Lecture # 7 - Client & Server Communication

## Lecture Topics

- Adding React to Flask
- CORS (Cross-Origin Resource Sharing)
- How to proxy the requests to our API

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

6. In another terminal, run `npm install --prefix client` in your terminal to install the dependencies from the `package.json` file.

7. Run `npm start` in your terminal to run this React app in the browser. If your browser does not automatically open the page for you, open [http://localhost:4000](http://localhost:4000) to view it in your browser.