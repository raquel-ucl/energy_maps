from energy_app import app
from flask import url_for, render_template
from DataPlotter import DataPlotter

@app.route('/')
@app.route('/graph/')
@app.route('/graph/<graph>')
def layout(graph=None):
    return render_template('graph.html')

@app.route('/plot')
def show_plot():
    plotter = DataPlotter()
    graph = plotter.get_graph()
    return render_template('plot.html', graph=graph)

@app.route('/map')
def show_map():
    return render_template('map.html')

@app.route('/company/<company>')
def show_company(company):
    # show the user profile for that user
    return 'Company %s' % company

@app.route('/tweet/<int:tweet_id>')
def show_tweet(tweet_id):
    # show the post with the given id, the id is an integer
    return 'Tweet %d' % tweet_id

# with app.test_request_context():
#     print url_for('layout')
#     print url_for('show_company', company="edfenergy")
#     print url_for('show_tweet', tweet_id="23")
#     print url_for('static', filename='style.css')
