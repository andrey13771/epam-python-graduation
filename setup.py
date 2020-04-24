from setuptools import setup, find_packages

setup(
    name='department_app',
    version='1.0.0',
    description='A simple web app for managing departments and employees',
    author='Andrii Pavlenko',
    author_email='andrey13771@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask-migrate',
    ]
)
