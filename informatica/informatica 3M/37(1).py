from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('links.json', 'r') as f:
        links = json.load(f)
    return render_template('index.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
