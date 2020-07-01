from flask import render_templ
from mysite import app



@app.route ('/')
@app.route ('/index')
def index ():
    return render_template('index.html')
