from flask import Flask, request, jsonify, g
from db import get_db
from flask_cors import CORS, cross_origin
import service.auth as authService
import service.file as fileService
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    return authService.register()


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    return authService.login()

@app.route('/sendDocument', methods=['POST'])
@cross_origin()
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
