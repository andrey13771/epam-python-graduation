import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join('department_app', 'migrations'))

    @app.route('/health')
    def health():
        return {'status': 'ok'}

    return app


from department_app.models import models
from department_app.views import routes
