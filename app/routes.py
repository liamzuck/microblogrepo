from flask import render_template
from app import app

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
