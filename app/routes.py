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
            'author':  'John',
            'body': 'Motivation is what keeps you going it cane be positive or negative!'
        },
        {
            'category':'Interview',
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!'
        },
        {
            'category':'Promotion',
            'author':'Melody',
            'body':'Take time to ptomote people in life'
        },
        {
            'category':'Interview',
            'author':'Khan',
            'body':'Interviews makes you strong'
        }
    ]  
    return render_template('index.html',user = user,pitches = pitches)
