from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/graph/')
@app.route('/graph/<graph>')
def layout(graph=None):
    return render_template('graph.html', graph=graph)

@app.route('/company/<company>')
def show_company(company):
    # show the user profile for that user
    return 'Company %s' % company

@app.route('/tweet/<int:tweet_id>')
def show_tweet(tweet_id):
    # show the post with the given id, the id is an integer
    return 'Tweet %d' % tweet_id

with app.test_request_context():
    print url_for('layout')
    print url_for('show_company', company="edfenergy")
    print url_for('show_tweet', tweet_id="23")
    print url_for('static', filename='style.css')


if __name__ == '__main__':
    app.run()
