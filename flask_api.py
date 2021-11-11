from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

# Our API will have two endpoints, users and locations

# To create an endpoint, we define a python class.
# Flask needs to know that this class is an endpoint for our API, and so we pass Resource in with the class definition.

class Users(Resource):
    # methods go here
    pass


class Locations(Resource):
    # methods go here
    pass


api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()  # run our Flask app