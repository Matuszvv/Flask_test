from flask import Flask, jsonify, render_template, url_for
from flask.json.tag import TaggedJSONSerializer

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'hello': 'world'})

if __name__ == "__main__":
    app.run(debug=True)

