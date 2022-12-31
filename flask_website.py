from flask import Flask
from flask import request
from flask import render_template


#initialize global variable
APP = Flask(__name__, template_folder='templates', static_folder='static')


@APP.route('/')
def main():
    return render_template('index.html')


@APP.route('/login', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        uname = request.form['uname']
        pword = request.form['pword']
    return render_template('action_page.html', uname=uname, pword=pword)


if __name__ == '__main__':
    APP.run(debug=True)


#to start run
#export FLASK_APP=name_of_flask_file
#flask run