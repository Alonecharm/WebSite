# encoding:utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import app
from exstense import db

manager = Manager(app)

migrate = Migrate(app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()