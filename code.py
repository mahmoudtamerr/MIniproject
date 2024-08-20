from gpiozero import DistanceSensor 
from gpiozero import Servo
from datetime import datetime
import blynklib
BLYNK_AUTH = "CpYEPIeI5E7quu9_CuVJlcsoXdOmcblI"
def getTime():
    return float(str(datetime.now().time()).split(':')[2])

sensor = DistanceSensor(echo=15,trigger=16)
servo = Servo(5)
opened = 0
start = 0
while True:
    inputCommand = input()
    if inputCommand =="on" :
        servo.max()
        opened = 1
    elif inputCommand=="off":
        servo.min()
        opened = 0
    if sensor.distance < 0.1 : 
        if not start and opened :
            start = 1
            time_when_door_closed = getTime()
            if opened and getTime() - time_when_door_closed > 10.0:
                servo.min()
                opened = 0
                start = 0
                

