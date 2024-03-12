from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def top():
    return render_template('/home.html')

@app.route('/menu')
def menu():
    return render_template('/menu.html')

@app.route('/seats')
def seets():
    return render_template('/seats.html')

@app.route('/access')
def access():
    return render_template('/access.html')

if __name__ == '__main__':
    app.run(debug=True)