from flask import Flask

app = Flask(__name__)

intro = "This is the Home."

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return intro

if __name__ == '__main__':
    app.run(debug=True)