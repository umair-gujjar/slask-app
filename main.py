"""`main` is the top level module for your Flask application."""

import logging

# Import the Flask Framework
from flask import Flask, render_template

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    logging.debug('this is a debug message.')
    return render_template('hello.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL. ({})'.format(e), 404


@app.errorhandler(500)
def unexpected_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
