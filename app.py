# from flask import Flask, render_template
import flask
app = flask.Flask(__name__)
import json

site_name = 'themichaelwilson.com'


@app.route('/')
def index():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('index.html', site_name=site_name)

@app.route('/api/test')
def api_test():
    sample_obj = {
        "name": "Michael Wilson",
        "age": 28,
        "occupation":"Support Engineer"
    }
    return app.response_class(
        response=json.dumps(sample_obj),
        status=200,
        mimetype='application/json'
    )
# @app.route('/underconstruction')
# def construction_function():
#     flask.url_for('static', filename='css/bootstrap.min.css')
#     return flask.render_template('underconstructionpage.html')

@app.route('/ads.txt')
def construction_function():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('ads.html')

@app.route('/prebid_long_code_test')
def construction_function():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('longcodetest.html')

if __name__ == "__main__":
    app.run()
