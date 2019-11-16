from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json

app = Flask(__name__)

def getTodos():
    with open('todos.json', encoding="utf8") as json_file:
        return json.load(json_file)

def getTodo(id):
    todos = getTodos()
    return next(filter(lambda x: x['id'] == int(id), todos))

def addTodo(todo):
    todos = getTodos()
    todos.append(todo)
    with open('todos.json', 'w', encoding="utf8") as json_file:
        return json.dump(todos, json_file, ensure_ascii = False)

def toggleTodo(id):
    todos = getTodos()
    todo = next(filter(lambda x: x['id'] == int(id), todos))
    todo['status'] = abs(todo['status'] - 1)
    with open('todos.json', 'w', encoding="utf8") as json_file:
        return json.dump(todos, json_file, ensure_ascii = False)

def deleteTodo(id):
    todos = getTodos()
    # todos = list(filter(lambda x: x['id'] != int(id), todos))
    todos = list([x for x in todos if x['id'] != int(id)])
    with open('todos.json', 'w', encoding="utf8") as json_file:
        return json.dump(todos, json_file, ensure_ascii = False)

def updateTodo(todo_toedit):
    todos = getTodos()
    todo = next(filter(lambda x: x['id'] == int(todo_toedit['id']), todos))
    todo['name'] = todo_toedit['name']
    with open('todos.json', 'w', encoding="utf8") as json_file:
        return json.dump(todos, json_file, ensure_ascii = False)


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        now = datetime.now()
        todo_name = request.form.get('todo_name')
        todoDict = {
            'id': int(datetime.timestamp(now)),
            'name' : todo_name,
            'status': 0,
            'create_at': now.strftime("%d-%m-%Y %H:%M:%S"),
            'deadline': None
        }
        addTodo(todoDict)
    return render_template('index.html', todos=getTodos())

@app.route('/toggle/<id>')
def toggle(id):
    toggleTodo(id)
    return redirect(url_for('index'))


@app.route('/delete/<id>')
def delete(id):
    deleteTodo(id)
    return redirect(url_for('index'))


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    todo = getTodo(id)
    if request.method == 'POST':
        todo_name = request.form.get('todo_name')
        todo['name'] = todo_name
        updateTodo(todo)
        return redirect(url_for('index'))
    return render_template('edit.html', todo=todo)

if __name__ == '__main__':
    app.run(debug=True)
