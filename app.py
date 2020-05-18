from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from user import UserRegister #import UserRegister which is our resource
from item import Item # Item is the name of the file we have created

app = Flask(__name__)
app.secret_key = 'mahendra'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register') #when POST request is execute, UserRegister willl be called and it will be called in user.def foo():

if __name__ == '__main__':
    app.run(debug=True)
