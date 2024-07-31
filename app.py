from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message='Hello, Flask!')

@app.route('/OrderDHA')
def OrderDHA():
    return render_template("DHA.html")

if __name__ == '__main__':
    app.run(debug=True)
