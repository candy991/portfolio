from flask import Flask, render_template, request

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

@app.route('/大皿')
def oozara():
    return render_template('/大皿.html')

if __name__ == '__main__':
    app.run(debug=True)