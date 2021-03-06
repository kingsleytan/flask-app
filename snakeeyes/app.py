from flask import Flask
from snakeeyes.blueprints.page import page


def create_app(settings_override=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    # silent=True to avoid overriding production settings

    if settings_override:
        app.config.update(settings_override)
    app.register_blueprint(page)

    return app
