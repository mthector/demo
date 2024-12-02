from flask import Flask, abort, render_template, request, redirect
from forms.task_form import TaskForm

import config as custom_config

from databases.data import tasks, find_task, delete_task
from databases.db import db, Task, Category



app = Flask(__name__)
app.config.from_object(custom_config)
db.init_app(app)



@app.route('/')
def hello():
    return 'Hello World! Im Hector, from 2ASIR'



@app.route('/list/')
def list():
    tasks = Task.query.all()
    return render_template('all_tasks.html', tasks = tasks)



@app.route('/task/<int:id>/')
def details(id):
    tasks = Task.query.filter_by(id=id).first()

    if tasks:
        return render_template('details.html',task = tasks)
    else:
        abort(404)



@app.route('/task/<int:id>/delete/')
def delete(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect('/list/')



@app.route('/task/<int:id>/update/', methods=["GET","POST"])
def update(id):
    task = Task.query.filter_by(id=id).first()
    form = TaskForm(request.form, obj=task)
    form.category_id.choices = [(category.id, category.name) for category in Category.query.all()]

    if form.validate() and request.method == "POST":
        task.name = form.name.data
        task.description = form.description.data
        task.due_date =  form.due_date.data
        task.category_id = form.category_id.data
        db.session.commit()
        return redirect ('/list/')
    
    return render_template('task_from.html', form = form)



@app.route('/task/create/', methods=['GET', 'POST'])
def create():
    form = TaskForm(request.form)
    form.category_id.choices = [(category.id, category.name) for category in Category.query.all()]
    if form.validate() and request.method == "POST":
        task = Task(
            name = form.name.data,
            description = form.description.data,
            due_date =  form.due_date.data,
            category_id = form.category_id.data
        )
        db.session.add(task)
        db.session.commit()
        return redirect('/list/')
    
    return render_template('create_task.html', form = form)