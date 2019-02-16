from flask import Flask, render_template

app = Flask(__name__)

#app.config.from_pyfile('settings.py')
@app.route('/')


def index():
    return render_template("index.html")

#def hello_world():
#    return ('hello world my love')

if __name__ == "__main__":
    app.run(debug=True)
