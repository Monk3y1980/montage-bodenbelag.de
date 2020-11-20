from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/free-consultation', methods=['GET', 'POST'])
def contact_consultation():
    pass


@app.route('/inquiry', methods=['GET', 'POST'])
def contact_consultation():
    pass


if __name__ == '__main__':
    app.run(debug=True)
