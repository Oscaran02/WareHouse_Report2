import os

from flask import render_template, redirect, url_for, Flask, request
from flask_cors import CORS

from models import report

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)
app.config["DEBUG"] = True
app.config['host'] = '0.0.0.0'
app.config['port'] = 5000
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

report_data = report("0", "0", "Colombia")
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
    return report_data.average_times_in_warehouse().to_json(orient='records')


# Segunda gráfica - Estado
@app.route("/data2", methods=['GET'])
def data2():
    pass


# Tercera gráfica - Estado transito
@app.route("/data3", methods=['GET'])
def data3():
    pass


# Cuarta gráfica - Prealerta
@app.route("/data4", methods=['GET'])
def data4():
    pass


# Quinta gráfica - Origen
@app.route("/data5", methods=['GET'])
def data5():
    pass


# Sexta gráfica - Courier internacional
@app.route("/data6", methods=['GET'])
def data6():
    pass


# Séptima gráfica - Alianzas
@app.route("/data7", methods=['GET'])
def data7():
    pass


# Octava gráfica - Courier local
@app.route("/data8", methods=['GET'])
def data8():
    pass


# Novena gráfica - Departamentos
@app.route("/data9", methods=['GET'])
def data9():
    pass

# Décima gráfica - Tiempos totales
@app.route("/data10", methods=['GET'])
def data10():
    pass
