from datetime import datetime
from department_app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return f'<Department {self.title}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title
            # TODO _links
        }
        return data

    def from_dict(self, data):
        for field in ['title']:
            if field in data:
                setattr(self, field, data[field])


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    dob = db.Column(db.Date, index=True)
    salary = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return f'<Employee {self.name}>'

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'dob': self.dob.isoformat(),
            'salary': self.salary,
            'department_id': self.department_id
            # TODO _links
        }
        return data

    def from_dict(self, data):
        for field in ['name', 'salary', 'department_id']:
            if data[field]:
                setattr(self, field, data[field])
        if data['dob']:
            self.dob = datetime.strptime(data['dob'], '%Y-%m-%d').date()
