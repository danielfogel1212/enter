from flask import Flask, render_template, request, redirect, url_for,jsonify,session
from flask_sqlalchemy import SQLAlchemy
import locale

from datetime import datetime
from flask_cors import CORS
from flask_session import Session
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies


app = Flask(__name__)


app.config['SECRET_KEY'] = '1234'


# Configure the MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sctime'
CORS(app)
db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)
 
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = password
        
 
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    morning = db.Column(db.String(80), nullable=False)
    lunch = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    dates = db.Column(db.String(80),unique=False, nullable=False)
    day= db.Column(db.Integer, unique=False,nullable=False)
 
 
    def __init__(self, morning, lunch, user_id, dates,day):
        self.morning = morning
        self.lunch = lunch
        self.user_id = user_id
        self.dates = dates
        self.day = day
 
with app.app_context():
    db.create_all()
 
def logout():
    response = jsonify({'message': 'Logout successful'})
    unset_jwt_cookies(response)
    return response, 200

class UserLogin(Resource):
    def post(self):
        data= request.form


        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user and user.id==11:
            # Assuming successful authentication
            access_token = create_access_token(identity=user.id)
            return {'message': 'Login successful', 'access_token': access_token}, 200
        elif user:
             access_token = create_access_token(identity=user.id)
             return {'message': 'Login ', 'access_token': access_token}, 201
        else:
            return {'message': 'no user found'}, 401
        

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {'message': f'Hello, {current_user}!'}
    

class Admin(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print(current_user)
        print(current_user)
        if current_user == 11:
            return {'message': 'Hello, logged in successfully!'}, 200
        else:
            return {'message': 'Unauthorized'}, 401

api.add_resource(UserLogin, '/login')
api.add_resource(ProtectedResource, '/protected')
api.add_resource(Admin, '/admin')

 
if __name__ == '__main__':
    app.run(debug=True)
