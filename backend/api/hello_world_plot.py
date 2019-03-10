import json

import numpy as np
from flask import Blueprint, jsonify
from flask_restplus import Resource, Api, reqparse

API_VERSION_V1 = 1

api_bp = Blueprint('api', __name__)
api_v1 = Api(api_bp)

parser = reqparse.RequestParser()


class HelloFlaskPlotyVue(Resource):

    def get(self):
        parser.add_argument('stop', type=int, default=10)
        parser.add_argument('num', type=int, default=30)
        args = parser.parse_args()
        stop = args.get('stop', 10)
        num = args.get('num', 30)

        x = np.linspace(0, stop, num=num)
        y = np.sin(x)
        return jsonify({'x': x.tolist(), 'y': y.tolist()})


api_v1.add_resource(HelloFlaskPlotyVue, '/sin')
