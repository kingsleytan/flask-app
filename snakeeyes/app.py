from flask import Flask


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True) # silent=True to avoid overriding production settings

    @app.route('/')
    def index():
        a = "1"
        return app.config['HELLO']

    return app
