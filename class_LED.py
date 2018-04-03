import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

led_r = 16
led_g = 20
led_b = 21
GPIO.setup(led_r, GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(led_g, GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(led_b, GPIO.OUT,initial = GPIO.LOW)
        

class LED:    
    def __init__(self):
        pass
        
   
        
        
        