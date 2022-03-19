from flask import render_template, flash, redirect, url_for
from app import apl
from app.forms import LoginForm

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

@apl.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)