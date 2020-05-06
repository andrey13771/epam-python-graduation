from flask import jsonify
from flask_restful import Resource, reqparse
from department_app.models.models import Department as Dep, Employee as Emp
from department_app import db

parser_dep = reqparse.RequestParser()
parser_dep.add_argument('title')
parser_emp = reqparse.RequestParser()
parser_emp.add_argument('name')
parser_emp.add_argument('dob')
parser_emp.add_argument('salary')
parser_emp.add_argument('department_id')


class Department(Resource):

    def get(self, department_id):
        return Dep.query.get_or_404(department_id).to_dict()

    def delete(self, department_id):
        department = Dep.query.get_or_404(department_id)
        db.session.delete(department)
        db.session.commit()
        return '', 204

    def put(self, department_id):
        args = parser_dep.parse_args()
        department = Dep.query.get_or_404(department_id)
        department.from_dict(args)
        db.session.commit()
        response = jsonify(department.to_dict())
        response.status_code = 201
        return response


class DepartmentList(Resource):

    def get(self):
        return [dep.to_dict() for dep in Dep.query.all()]

    def post(self):
        args = parser_dep.parse_args()
        department = Dep()
        department.from_dict(args)
        db.session.add(department)
        db.session.commit()
        response = jsonify(department.to_dict())
        response.status_code = 201
        # TODO response.headers['Location'] =
        return response


class Employee(Resource):

    def get(self, employee_id):
        return jsonify(Emp.query.get_or_404(employee_id).to_dict())

    def delete(self, employee_id):
        employee = Emp.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return '', 204

    def put(self, employee_id):
        args = parser_emp.parse_args()
        employee = Emp.query.get_or_404(employee_id)
        employee.from_dict(args)
        db.session.commit()
        response = jsonify(employee.to_dict())
        response.status_code = 201
        return response


class EmployeeList(Resource):

    def get(self):
        return jsonify([emp.to_dict() for emp in Emp.query.all()])

    def post(self):
        args = parser_emp.parse_args()
        employee = Emp()
        employee.from_dict(args)
        db.session.add(employee)
        db.session.commit()
        response = jsonify(employee.to_dict())
        response.status_code = 201
        # TODO response.headers['Location'] =
        return response
