
devices = ['Front Door', 'Garage']

check_connect = {
    'Front Door': [],
    'Garage': [],
}

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





