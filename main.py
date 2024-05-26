from flask import Flask, request, jsonify, g
from db import get_db
import service.auth as authService
import service.file as fileService
app = Flask(__name__)


@app.route('/register', methods=['POST'])
def register():
    return authService.register()


@app.route('/login', methods=['POST'])
def login():
    return authService.login()

@app.route('/sendDocument', methods=['POST'])
def sendDocument():
    return fileService.sendDocx()

@app.before_request
def before_request():
    g.db = get_db()


@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
