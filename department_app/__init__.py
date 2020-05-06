import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config


db = SQLAlchemy()
migrate = Migrate()
api = Api()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    from .rest import bp as api_bp

    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join('department_app', 'migrations'))
    api.init_app(api_bp)

    api.add_resource(DepartmentList, '/departments')
    api.add_resource(Department, '/departments/<department_id>')
    api.add_resource(EmployeeList, '/employees')
    api.add_resource(Employee, '/employees/<employee_id>')

    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/health')
    def health():
        return {'status': 'ok'}

    return app


from .models import models
from .rest.api import Department, DepartmentList, Employee, EmployeeList
from .views.main import routes
