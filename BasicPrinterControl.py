import RPi.GPIO as GPIO
import time
rightMotor=10
leftMotor=11
rightDirection=GPIO.HIGH
leftMotorDirection=GPIO.HIGH
GPIO.setmode(GPIO.BCM)
GPIO.setup(rightMotor, GPIO.OUT)
GPIO.setup(leftMotor, GPIO.OUT)
motorList=(rightMotor, leftMotor)

for x in range(0,100):
    pulse()
    GPIO.output(motorList, GPIO.HIGH)

def rightMotorDirection(direction=True):
    if direction:
        GPIO.output(rightMotorDirection, GPIO.HIGH)
    else:
        GPIO.OUTPUT(rightMotorDirection, GPIO.LOW)

def leftMotorDirection(direction=True):
    if direction:
        GPIO.output(leftMotorDirection, GPIO.HIGH)
    else:
        GPIO.OUTPUT(leftMotorDirection, GPIO.LOW)

def pulse():
    GPIO.output(motorList, pulseIndex)
    time.sleep(0.0001)
    GPIO.output(motorList, (GPIO.LOW, GPIO.LOW))
    time.sleep(0.0001)

def pulseIndex(Right,Left):
    return (GPIO.HIGH if Right else GPIO.LOW, GPIO.HIGH if Left else GPIO.LOW)

def pulseRatio(motor,):
