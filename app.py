from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Jay yogeshwar!! </h1>"

@app.route('/about')
def about():
    return "<h1> About </h1>"

if __name__ == '__main__' :
    app.run(debug=True)


