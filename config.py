#encoding:utf-8

import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'website'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = f'mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'

SQLALCHEMY_DATABASE_URI = DB_URI
