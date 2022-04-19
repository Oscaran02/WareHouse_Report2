import os
from time import sleep

from flask import render_template, redirect, url_for, Flask, request
from flask_cors import CORS

from models import report

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)
app.config["DEBUG"] = False
app.config['host'] = '0.0.0.0'
app.config['port'] = 5000
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

report_data = report("0", "0", "Colombia")


@app.route("/")
@app.route("/home")
@app.route("/dashboard")
def dashboard():
    report_data.set_data()
    return render_template("dashboard.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = f.filename.split('.')[1]
        f.filename = "data." + f.filename
        filename = (os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        f.save(filename)
        f.close()
        report_data.set_data()
        return redirect(url_for('dashboard'))


# Primera gráfica
@app.route("/promedios_bodega", methods=['GET'])
def promedios_bodega():
    sleep(0.1)
    return report_data.average_times_in_warehouse().to_json(orient='records')


# Segunda gráfica - Estado
@app.route("/data2", methods=['GET'])
def data2():
    sleep(0.3)
    return report_data.state_of_package().to_json()


# Tercera gráfica - Estado transito
@app.route("/data3", methods=['GET'])
def data3():
    sleep(0.6)
    return report_data.state_of_package_in_transit().to_json()


# Cuarta gráfica - Prealerta
@app.route("/data4", methods=['GET'])
def data4():
    sleep(0.9)
    return report_data.prealerts().to_json()


# Quinta gráfica - Origen
@app.route("/data5", methods=['GET'])
def data5():
    sleep(1.3)
    return report_data.origin_of_package().to_json()


# Sexta gráfica - Courier internacional
@app.route("/data6", methods=['GET'])
def data6():
    sleep(1.6)
    return report_data.international_courier().to_json()


# Séptima gráfica - Alianzas
@app.route("/data7", methods=['GET'])
def data7():
    sleep(1.9)
    return report_data.alliance_of_package().to_json()


# Octava gráfica - Courier local
@app.route("/data8", methods=['GET'])
def data8():
    sleep(2.2)
    return report_data.local_courier().to_json()


# Novena gráfica - Departamentos
@app.route("/data9", methods=['GET'])
def data9():
    sleep(2.5)
    return report_data.department_of_customer().to_json()


# Décima gráfica - Tiempos totales
@app.route("/data10", methods=['GET'])
def data10():
    sleep(2.8)
    return report_data.average_time_in_routes().to_json()
