from gpiozero import LightSensor, Buzzer
import time
import requests
import network_lib

ldr = LightSensor(4)
buzzer = Buzzer(17)

device_name = 'Garden'

my_id = {'device_id': device_name}
create_requests = requests.post(network_lib.construct_url("/api/v1/device/create"), json=my_id)
network_lib.send_request_async(network_lib.start_reporting_heartbeat, device_name)
while True:
    print(ldr.value)
    if ldr.value < 0.5:
        network_lib.send_request_async(network_lib.report_incident, device_name)
        buzzer.on()
    else:
        buzzer.off()
    time.sleep(0.1)


