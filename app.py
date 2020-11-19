from flask import Flask, render_template, request, url_for

app = Flask(__name__)

navbar = [{'name': 'Home', 'url': 'index.html'},
          {'name': 'Über uns', 'url': '#about'},
          {'name': 'Service', 'url': '#services'},
          {'name': 'Das Team', 'url': '#team'},
          {'name': 'Empfehlungen', 'url': '#empfehlung'},
          {'name': 'Kontakt', 'url': '#kontakt'}
          ]


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
