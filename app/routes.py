from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, HouseForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/songs')
def songs():
    user = {'username': 'Miguel'}
    songs = [{'title': 'Let it Be','artist': 'the Beatles'},{'title':'Billy Jean','artist': 'Michael Jackson'}]
    return render_template('songs.html', title='Songs', user=user, songs=songs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/willow', methods=['GET', 'POST'])
def willow():
    form = HouseForm()
    if form.validate_on_submit():
        flash('House ({}) posted for {}. For Sale = {}'.format(
            form.address.data, form.owner.data, form.for_sale.data))
        return redirect('/index')
    return render_template('willow.html', title='House Lising (Willow)', form=form)
