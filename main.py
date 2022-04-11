import os
from flask import render_template, redirect, url_for, Flask, request
from flask_cors import CORS
from models import report as rprt

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)
app.config["DEBUG"] = True
app.config['host'] = '0.0.0.0'
app.config['port'] = 5000
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx', 'csv'}


@app.route("/graph")
def graph():
    return render_template("graph.html")


@app.route("/")
def default():
    return redirect(url_for("upload"))


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = f.filename.split('.')[1]
        f.filename = "data."+f.filename
        filename = (os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        f.save(filename)
        return 'Archivo subido exitosamente'


@app.route("/data", methods=['GET'])
def data():
    report_data = rprt("0", "0", "Colombia")
    report_data.set_data()
    return report_data.df.to_json(orient='records')


if __name__ == '__main__':
    app.run()
