import unittest
from config import Config
from department_app import create_app, db


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestAppFactory(unittest.TestCase):
    pass


class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crud(self):
        params = [
            (
                {'title': 'test dept'},
                'departments', ('title',),
                {'title': 'test test'}
            ),
            (
                {'name': 'test', 'dob': '1970-01-01', 'salary': 10000, 'department_id': 1},
                'employees', ('name', 'dob', 'salary', 'department_id'),
                {'name': 'testing', 'dob': '1990-01-01', 'salary': 15000, 'department_id': 1}
            )
        ]
        for data, endpoint, args, new_data in params:
            with self.subTest(endpoint=endpoint):
                response = self.client.post(f'/api/{endpoint}', data=data)
                self.assertEqual(response.status_code, 201)
                for arg in args:
                    self.assertEqual(response.json[arg], data[arg])

                response = self.client.get(f'/api/{endpoint}')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, [{'id': 1, **data}])

                response = self.client.get(f'/api/{endpoint}/1')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {'id': 1, **data})

                response = self.client.put(f'/api/{endpoint}/1', data=new_data)
                self.assertEqual(response.status_code, 201)
                self.assertEqual(response.json, {'id': 1, **new_data})

                response = self.client.delete(f'/api/{endpoint}/1')
                self.assertEqual(response.status_code, 204)
                self.assertEqual(response.data, b'')
