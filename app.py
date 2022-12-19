import os

from flask import Flask
from flask_smorest import Api

from resources.db import db
import Models

def create_app(db_url=None):

    app = Flask(__name__)

    app.config['PROPAGATE_EXCEPTIONS']=True
    app.config['API_TITLE']='Stores REST API'
    app.config['API_VERSION']='v1.0.0'
    app.config['OPENAPI_VERSION']='3.0.3'
    app.config['OPENAPI_URL_PREFIX']='/'
    app.config['OPENAPI_SWAGGER_UI_PATH']='/docs/swagger'
    app.config['OPENAPI_SWAGGER_UI_URL']='https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui-bundle.js'

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.__init__(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    api=Api(app)

    return app