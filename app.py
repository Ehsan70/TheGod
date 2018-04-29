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
    return render_template('success.html', msg=msg)


@app.route('/pushmsg', methods=['POST', 'GET'])
def pushmsg():
    if request.method == 'POST':
        msg = request.form['formmsg']
        # todo make sure the message is not null
        msgdata = {
            "body": msg
        }
        results = db.child('messages').push(msgdata)
        return redirect(url_for('success', msg=msg))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/messages')
def getmsgs():
    msgs = db.child('messages').get()
    listmsgs = []
    for item in msgs.each():
        listmsgs.append(item.val()['body'])
    return render_template('messages.html', msgs=listmsgs)


if __name__ == '__main__':
    app.run()
