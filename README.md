# Flask-Vue Plotly Examples

Flask Plotly Examples

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- pipenv installed globally
- npm and yarn installed globally

### Installing

Build your python environment `pipenv install`
Build your javascript env, `cd frontend` install packages.

I root directory add a `.env` file with the following,

```
FLASK_ENV='development'
FLASK_APP='backend.app'
```

## Running the Example

1. Start your flask server up, `pipenv run flask run`.
2. Start your js dev server up, `yarn serve`.
3. Navigate to `http://localhost:8080/`, or whatever port `yarn serve` uses.

## Built With

* [Flask](http://flask.pocoo.org/) - Flask web framework
* [Flask-restplus](https://flask-restplus.readthedocs.io/en/stable/) - Flask-restplus for Api's
* [Numpy](http://www.numpy.org/) - Generating Data
* [Vue](https://vuejs.org/) - Front end
* [Axios](https://github.com/axios/axios) - Consuming backend API's
* [Plotly](https://plot.ly/javascript/) - Creating plots
* [Vue-Plotly](https://github.com/statnett/vue-plotly) - Vue wrapper for plotly
