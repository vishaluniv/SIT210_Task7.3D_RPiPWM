import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGG=21
ECHO=15
LEDP=19

GPIO.setup(TRIGG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LEDP,GPIO.OUT)

ledPWM = GPIO.PWM(LEDP,100)

ledPWM.start(0)

def ultrasonic():
    GPIO.output(TRIGG,False)

    time.sleep(0.2)
    GPIO.output(TRIGG, True)

    time.sleep(0.0001)
    GPIO.output(TRIGG, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()

    DurationTime = StopTime-StartTime

    distance = (DurationTime*34300)/2

    print(distance)
    return distance

def PWM_led(dist):
    if(dist<20):
        ledPWM.ChangeDutyCycle(round(100-(dist*5)))
        print("duty cycle updated: " + str(round(100-(dist*5))))
    else:
        ledPWM.ChangeDutyCycle(0)

try:
    while True:
        dista = ultrasonic()
        PWM_led(dista)
        time.sleep(0.1)
except KeyboardInterrupt:
    ledPWM.stop()
    print("---operation ceased---")
    GPIO.cleanup()
