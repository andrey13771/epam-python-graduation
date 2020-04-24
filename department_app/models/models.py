from department_app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return f'<Department {self.title}>'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    dob = db.Column(db.Date, index=True)
    salary = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return f'<Employee {self.name}>'
