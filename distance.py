import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(1, GPIO.OUT)
GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(37, GPIO.IN)


while True:
  p1 = GPIO.input(31)
  p2 = GPIO.input(33)
  p4 = GPIO.input(35)
  p8 = GPIO.input(37)
  print(str(8*p8+4*p4+2*p2+p1))
  time.sleep(0.0001)
