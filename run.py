import flask
from flask import Flask
app = Flask(__name__)


# Ugly static serve
@app.route('/main.js')
def script():
    return app.send_static_file('main.js')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/load.json')
def return_load():
    load ={
      "nodes":{
        "n-1":0.2,
        "n-2":0.1,
        "n-3":0.1,
        "n-4":0.1,
        "n-5":0.5
      },
      "links":[
        {"source": "n-1","target": "n-2"},
        {"source": "n-1","target": "n-3"},
        {"source": "n-1","target": "n-4"},
        {"source": "n-1","target": "n-5"},
        {"source": "n-2","target": "n-3"},
        {"source": "n-2","target": "n-4"},
        {"source": "n-2","target": "n-5"},
        {"source": "n-3","target": "n-4"},
        {"source": "n-3","target": "n-5"},
        {"source": "n-4","target": "n-5"}
      ],
      "current": "n-1"
    }
    return flask.jsonify(**load)

if __name__ == '__main__':
    app.run(debug = True)