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
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}


report_data = rprt("0", "0", "Colombia")
report_data.set_data()

@app.route("/")
@app.route("/home")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = f.filename.split('.')[1]
        f.filename = "data." + f.filename
        filename = (os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        f.save(filename)
        return redirect(url_for('dashboard'))


# Primera gráfica
@app.route("/promedios_bodega", methods=['GET'])
def promedios_bodega():
    return report_data.average_per_column_in_warehouse().to_json(orient='records')


# Segunda gráfica
@app.route("/data2", methods=['GET'])
def data2():
    pass


# Tercera gráfica
@app.route("/data3", methods=['GET'])
def data3():
    pass


# Cuarta gráfica
@app.route("/data4", methods=['GET'])
def data4():
    pass


# Quinta gráfica
@app.route("/data5", methods=['GET'])
def data5():
    pass


# Sexta gráfica
@app.route("/data6", methods=['GET'])
def data6():
    pass


# Séptima gráfica
@app.route("/data7", methods=['GET'])
def data7():
    pass


# Octava gráfica
@app.route("/data8", methods=['GET'])
def data8():
    pass
