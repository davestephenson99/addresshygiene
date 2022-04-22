from flask import Flask, request, render_template, json, jsonify, abort
from flask_restful import Resource, Api, reqparse
from flask_bootstrap import Bootstrap
from flask_cors import CORS

application = Flask(__name__)
CORS(application)


Bootstrap(application)
api = Api(application)


class AddressHygieneApi(Resource):

    def post(self):

        # This defines the expected POST variables (including a json payload)
        parser = reqparse.RequestParser()
        parser.add_argument('ADDRESS1', type=str)
        parser.add_argument('ADDRESS2', type=str)
        parser.add_argument('ADDRESS3', type=str)
        parser.add_argument('ADDRESS4', type=str)
        parser.add_argument('ADDRESS5', type=str)
        parser.add_argument('ADDRESS6', type=str)
        parser.add_argument('ADDRESS7', type=str)
        parser.add_argument('ADDRESS8', type=str)
        parser.add_argument('ADDRESS9', type=str)
        parser.add_argument('POSTCODE', type=str)
        args = parser.parse_args()

        # This sets the return values
        response['PAF_POBOX'] = ''
        response['PAF_ABODE'] = ''
        response['PAF_HOUSENAME'] = ''
        response['PAF_HOUSENUM'] = args['ADDRESS1']
        response['PAF_STREET1'] = args['ADDRESS2']
        response['PAF_STREET1TYPE'] = ''
        response['PAF_STREET2'] = args['ADDRESS3']
        response['PAF_SUBLOCALITY'] = ''
        response['PAF_LOCALITY'] = ''
        response['PAF_TOWN'] = args['ADDRESS4']
        response['PAF_POSTCODE'] = args['POSTCODE']
        response['PAF_DPS'] = ''
        response['PAFEXCEPTIONMESSAGE'] = 'OK'
        response['PAFENGINEDATE'] = 'Jan 2022'
        response['PAFSTATUS'] = 'OK'

        return jsonify(response)


api.add_resource(AddressHygieneApi, '/api/ahs', methods = ['POST']) # Route_1


@application.route("/")
def index():
      return render_template('index.html', status='OK')


if (__name__ == '__main__'):
        application.debug = True
        application.run()


