#importing flask
from flask import Flask, render_template, jsonify
#app is a flask object, name helps determine the root path
app = Flask(__name__)
# connecting all pages to python function/mapping


@app.route('/')
def index():
    return 'This is the homepage'


@app.route('/bookings')
def bookings():
    return render_template('sarah.html')


@app.route('/cv')
def resume():
    return 'This is the cv'


@app.route('/friends')
def friends():
    members = {'sam': [1, 2, 3], 'jane': [55, 699, 7]}
    return jsonify(members)

