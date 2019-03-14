from flask import Blueprint, jsonify
from flask_restplus import Resource, Api, reqparse

import numpy as np

API_VERSION_V1 = 1

monte_bp = Blueprint('monte', __name__)
monte_v1 = Api(monte_bp)

parser = reqparse.RequestParser()


class MontePlotData(Resource):

    def get(self):

        nSims = 1000
        # Create nSims of random walks
        walk_x = [np.arange(100, dtype='float64') for _ in range(nSims)]
        walk_y = [(np.random.rand(100) - 0.5).cumsum() for _ in range(nSims)]

        # concatinate segments into single line
        xs = np.concatenate(walk_x)
        ys = np.concatenate(walk_y)

        monte = {
            'x': xs.tolist(),
            'y': ys.tolist(),
            'mode': 'lines',
            'type': "scattergl",
            'opacity': 0.05,
            'line': {'color': 'darkblue'}
        }

        layout = {
            'title': f"Random Walk Plot with {nSims} simulations.",
            'showlegend': False
        }

        return jsonify({'data': monte, 'layout': layout})


monte_v1.add_resource(MontePlotData, '/monte')
