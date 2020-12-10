import requests

info = {'id':'pi', 'status':'connect', 'event':'OK'}
response = requests.post('http://192.168.0.16/api/v1/devices/device_info',
                        json= info )