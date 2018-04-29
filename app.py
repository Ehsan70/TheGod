from flask import Flask
from flask import render_template
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

@app.route('/pushmsg/<msg>')
def push_msg(msg):
    # todo make sure the message is not null
    msgdata = {
        "body": msg
    }
    results = db.child('messages').push(msgdata)
    return 'Message is {}. result is {}!'.format(msg, results)


@app.route('/fb')
def firebase():
    data = {"name": "Ehsa did this"}
    db.child("users").child("Morty").set(data)
    return "hi ehsan 222"

if __name__ == '__main__':
    app.run()
