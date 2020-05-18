import sqlite3 #importing sqlite3
from flask_restful import Resource, reqparse

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?,)" #NULL stands for auto increment
        cursor.execute(query, (data['username'],data['password'],))

        if User.find_by_username(data['username']):
            return {"message": "A user with this username already exists"}, 4000

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)" #NULL stands for auto incrementing
        cursor.excute(query, (data['username'],data['password'],))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201

class User: #present class has now a ability to interact with sqlite
    def __init__(self,_id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db') #create a new method to set and ability to find users by username
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?" #selects every row in the database but uses only the data that matches
        result = cursor.execute(query, (username,)) #since a single value tuple is necessary
        row = result.fetchone() #selects the first row out of results set
        if row:
            
            user = cls(*row)
        else:
            user = None #so we either receive a user object (if it exists) or None

        connection.close() #no need to commit since we have not added any data
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
