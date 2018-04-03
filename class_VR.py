import RPi.GPIO as GPIO
import spidev
import time

GPIO.setmode(GPIO.BCM)
#변수선언
AIN1=4
AIN2=25
PWMA=12
#듀티비 값
c_step=30
#각 변수 출력값
GPIO.setup(AIN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(AIN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(PWMA,GPIO.OUT,initial=GPIO.LOW)

p= GPIO.PWM(PWMA,100)
p.start(0)


#SPI
spi = spidev.SpiDev()
spi.open(0,1)
adc_read = [0, 0, 0]
adc_vol = [0, 0, 0]

class VR:
    def __init__(self):
        pass       

    def analog_read(self,ch):
        self.r = spi.xfer2([0x6 | (ch & 0x7) >>2, ((ch & 0x7) <<6), 0])
        self.adcout = ((self.r[1]&0xf) << 8)+ self.r[2]
        time.sleep(0.02)
        return self.adcout

    def get_vol(self,value):
        self.vol = ((3.3)*(value))/4095
        self.vol = float("{0:.2f}".format(self.vol))
        return self.vol

    def change_motor(self,x):
        GPIO.output(AIN1,GPIO.HIGH)
        GPIO.output(AIN2,GPIO.LOW)
        self.motor = 100*x/150
        #self.motor = int(self.motor)
        p.ChangeDutyCycle(self.motor)
        #print(self.motor)

'''  
if __name__=="main": 
    try:
        
        GPIO.output(AIN1,GPIO.HIGH)
        GPIO.output(AIN2,GPIO.LOW)
            
        while 1:
            adc_read[0]=self.analog_read(0)
            adc_read[1]=self.analog_read(1)
            adc_read[2]=self.analog_read(2)
            
            #adc_vol[0]=get_vol(int(adc_read[0]))
            adc_vol[1]=self.get_vol(int(adc_read[1]))
            #adc_vol[2]=get_vol(int(adc_read[2]))
          
            
            
         
            #print("[csd vr sound]")
            self.change_motor(adc_vol[1])
            print("VR:"+str(adc_read[1])+","+str(adc_vol[1])+"v")

            #print(adc_read)
            time.sleep(0.1)
            
            
    finally:
        spi.close()
'''     
    
