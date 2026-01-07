import RPi.GPIO as GPIO
import pygame
import time

pygame.joystick.init()
pygame.init()
joysticks=[pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

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


try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Example: print axis movements
                print(f"Axis {event.axis} moved to {event.value}")
            elif event.type == pygame.JOYBUTTONDOWN:
                # Example: print button presses
                print(f"Button {event.button} pressed")
            # ... handle other events like JOYHATMOTION, etc.

        # Add a small delay to prevent the loop from running too fast
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting")
    joystick.quit()
    pygame.quit()
else:
    print("No joysticks found")
    pygame.quit()
