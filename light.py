from gpiozero import LightSensor, Buzzer
import time

ldr = LightSensor(4)
buzzer = Buzzer(17)

while True:
    print(ldr.value)
    time.sleep(0.1)
    if ldr.value < 0.5:
        buzzer.on()
    else:
        buzzer.off()


