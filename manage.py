from flask import Flask
from demo import app, db
from databases.db import *
import config as custom_config

app = Flask(__name__)
app.config.from_object(custom_config)
db = SQLAlchemy(model_class=Base)
db.init_app(app)
app.config['DEBUG'] = True

def create_tables():
    "Create relational database tables"
    with app.app_context():
        db.create_all()


def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA"
    with app.app_context():
        db.drop_all()


def add_data_tables():
    with app.app_context():
        db.create_all()

        categories = [
            Category(name="Homeworks"),
            Category(name="Work"),
            Category(name="Academy"),
            Category(name="Sport")
        ]

        db.session.add_all(categories)
        db.session.commit()

        t1 = Task(name = "Task 1", description="You have to study IAW")
        t1.category_id = categories[0].id

        t2 = Task(name = "Task 2", description="You should do homework")
        t2.category_id = categories[0].id

        t3 = Task(name = "Task 3", description="Practice")
        t3.category_id = categories[1].id

        t4 = Task(name = "Task 4", description="More Practice")
        t4.category_id = categories[1].id

        t5 = Task(name = "Task 5", description="Make a virtual enviroment")
        t5.category_id = categories[2].id

        t6 = Task(name = "Task 6", description="Debug Your Code")
        t6.category_id = categories[2].id

        t7 = Task(name = "Task 7", description="Go to Gym", due_date=datetime.datetime.now())
        t7.category_id = categories[3].id


        db.session.add_all([t1, t2, t3, t4, t5, t6])
        db.session.commit()

if __name__ == '__main__':
    drop_tables()
    add_data_tables()