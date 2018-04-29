from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from config import Config
import pyrebase

config = {
    "apiKey": "AIzaSyCly_hMghY3hAMf8LEnbmpwvQ65uG2n_Nc",
    "authDomain": "thegod-1af4e.firebaseapp.com",
    "databaseURL": "https://thegod-1af4e.firebaseio.com",
    "projectId": "thegod-1af4e",
    "storageBucket": "thegod-1af4e.appspot.com",
    "messagingSenderId": "886710517455"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)
app.config.from_object(Config)


# todo remove pyrebase

@app.route('/')
@app.route('/index')
def hello_world():
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


@app.route('/success/<msg>')
def success(msg):
    return 'God heard you voice saying %s' % msg


@app.route('/pushmsg', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/fb')
def firebase():
    data = {"name": "Ehsa did this"}
    db.child("users").child("Morty").set(data)
    return "hi ehsan 222"


if __name__ == '__main__':
    app.run()
