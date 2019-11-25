from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template('<h2>welcome</h2>')


if __name__ == '__main__':
    app.run()