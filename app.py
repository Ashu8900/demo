from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)