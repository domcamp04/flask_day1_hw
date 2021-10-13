from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    top_five = ['Tiger Woods', 'Blackhawks', 'Cubs', 'Bears', 'Xander Schauffele']
    return render_template('favorites.html', top_five=top_five)