from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello world'


@app.route('/')
def i():
    return 'index'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/show')
def show(): pass


with app.test_request_context():
    print(url_for('show'))
    print(url_for('static', filename='index.css'))


@app.route('/template')
def index():
    return render_template('index.html')


@app.route('/template/<name>')
def temp(name):
    print(1)
    return render_template('temp.html', name=name)


if __name__ == '__main__':
    # app.debug = True
    # app.run(host='0.0.0.0')
    app.run()
