from flask import render_template, redirect, url_for, Flask
from flask_cors import CORS
from models import report as rprt

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)
app.config["DEBUG"] = True
app.config['host'] = '0.0.0.0'
app.config['port'] = 5000


@app.route("/graph")
def graph():
    return render_template("graph.html")


@app.route("/")
def default():
    return redirect(url_for("upload"))


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/data", methods=['GET'])
def data():
    report_data = rprt(0, 0, "Colombia")
    report_data.set_data()
    return report_data.df.to_json(orient='records')


if __name__ == '__main__':
    app.run()
