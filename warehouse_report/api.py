import os
from time import sleep

from flask import render_template, redirect, url_for, request, Blueprint, current_app as app

from . import models

api_bp = Blueprint('api', __name__, static_url_path="",
                   static_folder="static",
                   template_folder="templates"
                   )

report_data = models.report("0", "0", "Colombia")
report_data.set_data()


@api_bp.route("/")
@api_bp.route("/home")
@api_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api_bp.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = f.filename.split('.')[1]
        f.filename = "data." + f.filename
        filename = (os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        f.save(filename)
        f.close()
        report_data.set_data()
        # sleep(5)
        return redirect(url_for('api.dashboard'))


# Primera gráfica
@api_bp.route("/promedios_bodega", methods=['GET'])
def promedios_bodega():
    # sleep(0.5)
    return report_data.average_times_in_warehouse().to_json(orient='records')


# Segunda gráfica - Estado
@api_bp.route("/data2", methods=['GET'])
def data2():
    # sleep(1)
    return report_data.state_of_package().to_json()


# Tercera gráfica - Estado transito
@api_bp.route("/data3", methods=['GET'])
def data3():
    # sleep(1.5)
    return report_data.state_of_package_in_transit().to_json()


# Cuarta gráfica - Prealerta
@api_bp.route("/data4", methods=['GET'])
def data4():
    # sleep(2.0)
    return report_data.prealerts().to_json()


# Quinta gráfica - Origen
@api_bp.route("/data5", methods=['GET'])
def data5():
    # sleep(2.5)
    return report_data.origin_of_package().to_json()


# Sexta gráfica - Courier internacional
@api_bp.route("/data6", methods=['GET'])
def data6():
    # sleep(3)
    return report_data.international_courier().to_json()


# Séptima gráfica - Alianzas
@api_bp.route("/data7", methods=['GET'])
def data7():
    # sleep(3.5)
    return report_data.alliance_of_package().to_json()


# Octava gráfica - Courier local
@api_bp.route("/data8", methods=['GET'])
def data8():
    # sleep(4)
    return report_data.local_courier().to_json()


# Novena gráfica - Departamentos
@api_bp.route("/data9", methods=['GET'])
def data9():
    # sleep(4.5)
    return report_data.department_of_customer().to_json()


# Décima gráfica - Tiempos totales
@api_bp.route("/data10", methods=['GET'])
def data10():
    # sleep(5)
    return report_data.average_time_in_routes().to_json()
