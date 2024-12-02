from flask import abort


tasks = [
    {'id': 1,'name': 'Task0001', 'description': 'You have to study IAW', 'due_date': ''},
    {'id': 2,'name': 'Task0002', 'description': 'You should do homework', 'due_date': ''},
    {'id': 3,'name': 'Task0003', 'description': 'Practice', 'due_date': ''},
    {'id': 4,'name': 'Task0004', 'description': 'More Practice', 'due_date': ''},
    {'id': 5,'name': 'Task0005', 'description': 'Make a virtual enviroment', 'due_date': ''},
    {'id': 6,'name': 'Task0006', 'description': 'Debug your code', 'due_date': '28/10/24'},
]

def find_task(id):
    task = None

    for iterador in tasks:
        if iterador['id'] == id:
            task = iterador
    return task

def delete_task(id):
    index = 0
    index_to_remove = None

    for iterador in tasks:
        if iterador['id'] == id:
            index_to_remove = index
        index+=1

    if index_to_remove is None:
        abort(404)
    else:
        tasks.pop(index_to_remove)




