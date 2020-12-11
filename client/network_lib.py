import requests
import time
import threading
import urllib.parse

server_prefix = "http://34.94.27.195:2000/"

def construct_url(api):
    return urllib.parse.urljoin(server_prefix, api)

def send_request_async(func, device_name):
    threading.Thread(target=func, args=(device_name,)).start()

def report_incident(device_name):
    requests.post(construct_url("/api/v1/device/incident"), json={"device_id": device_name})

def start_reporting_heartbeat(device_name):
    while True:
        requests.post(construct_url("/api/v1/device/ping"), json={"device_id": device_name})
        time.sleep(0.5)
