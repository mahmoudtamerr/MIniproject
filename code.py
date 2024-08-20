from gpiozero import DistanceSensor 
from gpiozero import Servo
from datetime import datetime
import blynklib
BLYNK_AUTH = "CpYEPIeI5E7quu9_CuVJlcsoXdOmcblI" 
blynk = BlynkLib.Blynk(BLYNK_AUTH)
blynk = BlynkLib.Blynk(BLYNK_AUTH)

SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  
servo.start(0)

def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    servo.ChangeDutyCycle(0)

@blynk.VIRTUAL_WRITE(1)
def v1_write_handler(value):
    command = int(value[0]) 
    if command == 0:
        set_servo_angle(0)  
    elif command == 1:
        set_servo_angle(180)
def getTime():
    minutes = float(str(datetime.now().time()).split(':')[1])
    seconds = float(str(datetime.now().time()).split(':')[2])
    total = minutes*60 + seconds
    return int(total)

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
            if opened and getTime() - time_when_door_closed > 10:
                servo.min()
                opened = 0
                start = 0
                

