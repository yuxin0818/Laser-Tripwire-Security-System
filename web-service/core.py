from flask import Flask, request, jsonify, json, render_template
from database import add_device_id, add_device_info, check_exist, get_dictionary, get_id

app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route("/")
def hello_world():
    return render_template('index.html')


# pi api
@app.route('/api/v1/devices/device_info', methods=['POST'])
def get_device_info():
    req_data = request.get_json()

    device_id = req_data['id']
    device_status = req_data['status']
    device_event = req_data['event']

    if not check_exist(device_id):
        add_device_id(device_id)
        add_device_info(device_id, (device_status, device_event))
    else:
        add_device_info(device_id, (device_status, device_event))
        

    return jsonify({
        "status": "ok",
        })

@app.route('/api/v1/devices/incident_info', methods=['POST'])
def get_incident_status():
    incident_status = request.get_json()

    cur_status = incident_status['']

# serve javascript
@app.route('/scripts/monitor.js')
def get_scripts():
    return app.send_static_file('scripts/monitor.js')


# serve css
@app.route('/style4.css')
def get_css():
    return app.send_static_file('css/style4.css')

# script api
@app.route('/api/v1/request/get_id', methods=['GET'])
def request_id():
    key_list = get_id()
    return jsonify({
        "devices": key_list,
    })

@app.route('/api/v1/request/get_each_info', methods=['GET'])
def request_info():
    device_id = request.args.get('device_id')
    data_dict = get_dictionary()
    info_list = data_dict[device_id]
    return jsonify({
        "result": info_list,
    })
