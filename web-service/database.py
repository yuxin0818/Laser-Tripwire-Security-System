from enum import Enum
import time

'''
    DB = {
        key : {
            "last_ping_time": timestamp,
            "last_incident_time": timestamp,
            "reset_time": timestamp,
        },
    }
'''

LAST_PING_TIME = "last_ping_time"
LAST_INCIDENT_TIME = "last_incident_time"
RESET_TIME = "reset_time"

db = {
}

all_devices = []

class Status(Enum):
    OK = 1
    ERROR = 2


def create_new_device(device_id):
    if device_id not in db:
        all_devices.append(device_id)
        db[device_id] = {
            LAST_PING_TIME: 0,
            LAST_INCIDENT_TIME: 0,
            RESET_TIME: 0,
        }
        print("Device %s added successfully." % device_id)
        return Status.OK, None
    else:
        return Status.ERROR, "Device %s exists" % device_id

def record_incident(device_id):
    cur_time = time.time()
    if device_id not in db:
        return Status.ERROR, "Device %s does not exist" % device_id
    db[device_id][LAST_INCIDENT_TIME] = cur_time
    return Status.OK, None

def record_heartbeat(device_id):
    cur_time = time.time()
    if device_id not in db:
        return Status.ERROR, "Device %s does not exist" % device_id
    db[device_id][LAST_PING_TIME] = cur_time
    return Status.OK, None

def record_reset(device_id):
    cur_time = time.time()
    if device_id not in db:
        return Status.ERROR, "Device %s does not exist" % device_id
    db[device_id][RESET_TIME] = cur_time
    return Status.OK, None

def get_all_devices():
    return all_devices

def get_device_info(device_id):
    if device_id not in db:
        return Status.ERROR, "Device %s does not exist" % device_id, None
    return Status.OK, None, db[device_id]



