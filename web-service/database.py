from enum import Enum
import time

devices = ['Front Door', 'Garage']


'''
    DB = {
        key : {
            "last_ping_time": timestamp,
            "last_incident_time": timestamp,
            "reset_time": timestamp,
        },
    }
'''

db = {
    'Front Door': {},
    'Garage': {},
}

class Status(Enum):
    OK = 1
    ERROR = 2


def create_new_device(device_id):
    if device_id not in db:
        db[device_id] = {
            "last_ping_time": 0,
            "last_incident_time": 0,
            "reset_time": 0,
        }
        print("Device %s added successfully." % device_id)
        return Status.OK, None
    else:
        print("Device %s exists." % device_id)

def record_incident(device_id):
    cur_time = time.time()
    if device_id not in db:
        print("Device %s does not exist")
        return 

def add_device_id(id):
    check_connect[id] = []
    devices.append(id)

def add_device_info(id, info):
    current_info = get_current_device_info(id)
    current_info.append(info)
    check_connect[id] = current_info

def get_current_device_info(id):
    return check_connect[id]

def check_exist(id):
    return id in check_connect

def get_dictionary():
    print(check_connect)
    return check_connect

def get_id():
    return devices





