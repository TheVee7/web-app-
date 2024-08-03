from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message='Hello, Flask!')

@app.route('/OrderDHA')
def OrderDHA():
    return render_template("DHA.html")

@app.route("/OrderAssignments")
def OrderAssignment():
    return render_template("Assignment.html")

@app.route("/MoreOption")
def MoreOption():
    return render_template("more_opt.html")

@app.route('/download')
def download():
    return send_from_directory('static', 'TheHelpingApp.apk', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port= 5000)
