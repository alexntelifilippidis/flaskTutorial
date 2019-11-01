from flask import Flask, render_template, request
app = Flask(__name__)

todos = [
    {
        'name': 'Να παω supermarket',
        'status': 1,
        'created_at': '2019-10-30 10:10:00',
        'deadline': None
    },
    {
        'name': 'Τηλέφωνο στον πελάτη',
        'status': 0,
        'created_at': '2019-10-29 11:05:00',
        'deadline': '2019-11-01 11:05:00'
    },
    {
        'name': 'Να παω για κούρεμα',
        'status': 1,
        'created_at': '2019-10-31 17:13:00',
        'deadline': None
    },
    {
        'name': 'Να πληρώσω τη ΔΕΗ',
        'status': 1,
        'created_at': '2019-10-31 17:13:00',
        'deadline': None
    }
]

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = request.values.get('name', 'All')
    return render_template('index.html', todos=todos, name=name)

@app.route('/todolist/<name>')
def todolist(name):
    return render_template('todolist.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
