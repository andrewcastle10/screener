from app import app
from flask import Flask, render_template, flash, redirect, url_for

from bokeh.client import pull_session
from bokeh.embed import server_session, server_document
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():

    script = server_document(url='http://localhost:5006/FundScreener3.2')
    print("SUCCESS1")

    return render_template("embed.html", bokS=script, template="Flask")

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/help/')
def help():
    return render_template('help.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

