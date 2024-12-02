from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
import datetime

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Category(db.Model):
    """Categories of tasks"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    def __repr__(self):
        return {u'<{self.__class__.__name__}: {self.id}>'.format(self=self)}


class Task(db.Model):
    """Tasks of our application"""
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text(255),nullable=False,default=None)
    due_date = Column(DateTime,nullable=True,default=None)

    category_id=Column(Integer,ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", backref = "tasks")

    def countdown(self):
        return datetime.datetime.now() - self.due_date
