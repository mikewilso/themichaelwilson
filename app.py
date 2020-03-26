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
    return flask.render_template('ads.txt')

@app.route('/prebid_long_code_test')
def longcodetest_function():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('longcodetest.html')

@app.route('/hc_long_code_test')
def hclongcodetest_function():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('hclongcodetest.html')

@app.route('/display_tags_hardcoded')
def display_tags_hardcoded_function():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('displayads.html')

@app.route('/target_signal_footer_test')
def test_target_footer():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('footertargettest.html')

@app.route('/qa_page')
def qa_page():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('qatestpage.html')

@app.route('/test_page')
def test_page():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('oneadtestpage.html')

@app.route('/wes')
def wes_test_page():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('westest.html')

@app.route('/headercomplete')
def headercomplete_page():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('headercomplete.html')

@app.route('/sync')
def sync_test():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('synctest.html')

@app.route('/commerce_test')
def commerce_test():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('commerce.html')        

@app.route('/commerce_through_connect_test')
def commerce_in_connect_test():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('commerceconnecttest.html')

@app.route('/connect_commerce_sticky')
def commerce_sticky():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('commerceconnectstickyfooter.html')

@app.route('/commerce_through_connect_test_prod')
def commerce_in_connect_test_prod():
    flask.url_for('static', filename='css/bootstrap.min.css')
    return flask.render_template('commerceconnectprod.html')

@app.route("/.well-known/pki-validation/632BDE138705220EFF83EE038DC5A0FE.txt")
def file_sender():
    return flask.send_file('static/632BDE138705220EFF83EE038DC5A0FE.txt')


if __name__ == "__main__":
    app.run()
