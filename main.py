from flask import render_template, redirect, url_for, Flask
from flask_cors import CORS

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)
app.config["DEBUG"] = True
app.config['host'] = '0.0.0.0'
app.config['port'] = 5000


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/")
def default():
    return redirect(url_for("home"))


@app.route("/upload")
def upload():
    return render_template("upload.html")


if __name__ == '__main__':
    app.run()
