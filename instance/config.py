import os

SECRET_KEY = 'dev'

SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://amquvqrlcyjagn:205df9f4127051efb5c71af5fc8cb842adef79908a75b874e13e126403604f16@ec2-52-7-39-178.compute-1.amazonaws.com:5432/d9opv35ij85d7u')

