from unicodedata import category
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username' 'Melody'}
    pitches = [
        {
            'category':'Motivation',
            'author': {'username': 'John'},
            'body': 'Motivation is what keeps you going it cane be positive or negative!'
        },
        {
            'category':'Interview',
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'category':'Promotion',
            'author':{'username':'Melody'},
            'body':'Take time to ptomote people in life'
        },
        {
            'category':'Interview',
            'author':{'username':'Khan'},
            'body':'Interviews makes you strong'
        }
    ]  
    return render_template('index.html',user = user,pitches = pitches)
    