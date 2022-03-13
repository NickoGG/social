from flask import render_template
from app import apl

@apl.route('/')
@apl.route('/index')
def index():
    user = {'username': 'Nicko'}
    posts = [
        {
            'author': {'username': 'Mick'},
            'body': 'hello, everyone'
        },
        {
            'author': {'username': 'Joe'},
            'body': 'hey hey'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)