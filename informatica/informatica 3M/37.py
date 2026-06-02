import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_links():
    with open('37.json') as f:
        links = json.load(f)
    return render_template('37.html', links=links)

if __name__ == '__main__':
    app.run(debug=True, port=1234)
