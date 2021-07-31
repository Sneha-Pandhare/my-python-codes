from flask import Flask, render_template

flask_app = Flask(__name__)

@flask_app.route('/home')
def sendHomePage():
    return render_template('home.html')

@flask_app.route('/login')
def sendLoginPage():
    return render_template('login.html')

@flask_app.route('/something')
def sendSomethingPage():
    return render_template('something.html')

flask_app.run('0.0.0.0', 5000)

