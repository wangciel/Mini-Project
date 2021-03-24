from flask import Flask
from config import *

import Controllers_1_0


def create_app(config_name="develop"):
    app = Flask(__name__)
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    app.register_blueprint(Controllers_1_0.api, url_prefix='/api/1.0')
    return app
