from flask import Flask, request, render_template, json, jsonify, abort
from flask_restful import Resource, Api, reqparse
from flask_bootstrap import Bootstrap
from flask_cors import CORS

application = Flask(__name__)
CORS(application)


Bootstrap(application)
api = Api(application)


class AddressHygieneApi(Resource):
   def get(self):
       result = {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]}
       return result

api.add_resource(AddressHygieneApi, '/api/ahs') # Route_1


@application.route("/")
def index():
      return render_template('index.html')


if (__name__ == '__main__'):
        application.debug = True
        application.run()


