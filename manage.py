from multiprocessing import Manager
from flask import app
from app import create_app,db
from app.models import User
from flask_migrate import Migrate, MigrateCommand


app = create_app('prduction')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, user=User)

if __name__ =="__main__":
    manager.run()

