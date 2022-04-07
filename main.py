from flask import render_template, redirect, url_for, Flask
from flask_cors import CORS

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
CORS(app)
app.config["DEBUG"] = True


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/<name>")
def user(name):
    return f"Hello-- {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
