from flask import Blueprint, jsonify
from flask_restplus import Resource, Api, reqparse

import numpy as np
from scipy.ndimage.interpolation import shift
from statsmodels.tsa.stattools import acf


API_VERSION_V1 = 1

mva_bp = Blueprint('mva', __name__)
mva_v1 = Api(mva_bp)

parser = reqparse.RequestParser()


class MovingAverage(Resource):

    def get(self):
        parser.add_argument('phi', type=float, default=0.9)
        args = parser.parse_args()
        phi = args.get('phi', 0.9)

        Z = np.random.normal(size=1000)
        X = np.ones_like(Z)
        X[0] = Z[0]
        for i in range(1, 1000):
            X[i] = Z[i] + phi * X[i - 1]
        mva = [
            {
                'x': np.arange(1000).tolist(),
                'y': X.tolist(),
                'mode': 'lines+markers',
                'marker': {'size': 3}
            }

        ]
        autocorr_factors = acf(X)
        autocorr = [
            {
                'x': np.arange(len(autocorr_factors)).tolist(),
                'y': autocorr_factors.tolist(),
                'mode': 'lines+markers',
                'marker': {'size': 3}
            }
        ]
        return jsonify({'mva': mva, 'autocorr': autocorr})


mva_v1.add_resource(MovingAverage, '/mva')
