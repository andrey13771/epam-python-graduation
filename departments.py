from department_app import db, create_app
from department_app.models.models import Department, Employee

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Department': Department, 'Employee': Employee}
