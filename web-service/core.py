from flask import Flask, request, jsonify, json, render_template
import database
import logging

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

DEVICES_LABEL = "devices"
DEVICE_ID_LABEL = "device_id"
DEVICE_INFO_LABEL = "device_info"
STATUS_LABEL = "status"
STATUS_OK_LABEL = "OK"
STATUS_ERROR_LABEL = "ERROR"

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/api/v1/devices", methods=['GET'])
def get_all_devices():
    return jsonify({
        DEVICES_LABEL: database.get_all_devices(),
    })

@app.route("/api/v1/device/<device_id>", methods=['GET'])
def get_device_info(device_id):
    status, msg, info = database.get_device_info(device_id)
    if status != database.Status.OK:
        print("Failed to get the device info: %s" % msg)
        return jsonify({
            STATUS_LABEL: STATUS_ERROR_LABEL,
        })
    return jsonify({
        STATUS_LABEL: STATUS_OK_LABEL,
        DEVICE_INFO_LABEL: info,
    })   

@app.route("/api/v1/device/create", methods=['POST'])
def register_device():
    args = request.get_json()
    device_id = args[DEVICE_ID_LABEL]
    status, msg = database.create_new_device(device_id)
    if status != database.Status.OK:
        print("Failed to register the new device: %s" % msg)
        return jsonify({
            STATUS_LABEL: STATUS_ERROR_LABEL,
        })
    return jsonify({
        STATUS_LABEL: STATUS_OK_LABEL,
    })   

@app.route("/api/v1/device/incident", methods=['POST'])
def handle_incident():
    args = request.get_json()
    device_id = args[DEVICE_ID_LABEL]
    status, msg = database.record_incident(device_id)
    if status != database.Status.OK:
        print("Failed to record incident: %s" % msg)
        return jsonify({
            STATUS_LABEL: STATUS_ERROR_LABEL,
        })
    return jsonify({
        STATUS_LABEL: STATUS_OK_LABEL,
    })

@app.route("/api/v1/device/ping", methods=['POST'])
def handle_heartbeat():
    args = request.get_json()
    device_id = args[DEVICE_ID_LABEL]
    status, msg = database.record_heartbeat(device_id)
    if status != database.Status.OK:
        print("Failed to record ping: %s" % msg)
        return jsonify({
            STATUS_LABEL: STATUS_ERROR_LABEL,
        })
    return jsonify({
        STATUS_LABEL: STATUS_OK_LABEL,
    })

@app.route("/api/v1/device/reset", methods=['POST'])
def handle_reset():
    args = request.get_json()
    device_id = args[DEVICE_ID_LABEL]
    status, msg = database.record_reset(device_id)
    if status != database.Status.OK:
        print("Failed to record ping: %s" % msg)
        return jsonify({
            STATUS_LABEL: STATUS_ERROR_LABEL,
        })
    return jsonify({
        STATUS_LABEL: STATUS_OK_LABEL,
    })

# serve javascript
@app.route('/scripts/monitor.js')
def get_scripts():
    return app.send_static_file('scripts/monitor.js')

# serve css
@app.route('/style4.css')
def get_css():
    return app.send_static_file('css/style4.css')
