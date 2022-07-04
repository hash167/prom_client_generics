import os
from flask import Flask
from prom_client.flask import instrument_flask
app = Flask(__name__)
instrument_flask(app, "test_service")

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
