import RPi.GPIO as GPIO
import smbus2 as smbus
import time

bus = smbus.SMBus(1)
addr = 0x40

cmd_temp = 0xf3
cmd_humi = 0xf5
soft_reset = 0xfe
temp = 0.0
humi = 0.0
val = 0
data = [0,0,0]

class TempHumi:
    
    def __init__(self):
        bus.write_byte(addr,soft_reset)
        time.sleep(0.05)
        
    
    def get_temp(self):
        bus.write_byte(addr,cmd_temp)
        time.sleep(0.260)
        
        for i in range(0,3,1):
            data[i] = bus.read_byte(addr)
            
        val = data[0]<<8 | data[1]
        temp = -46.85 + 175.72 / 65536*val
        return temp

    def get_humi(self):
        
            
        bus.write_byte(addr,cmd_humi)
        time.sleep(0.260)
        
        for i in range(0,3,1):
            data[i] = bus.read_byte(addr)
        val = data[0] <<8 | data[1]
        humi = -6.0+125.0/65536*val
        return humi
        
def main():
    Temp = get_temp()
    Humi = get_humi()
    while True:
        print("temp level:"+str(temp.get_temp()))
        time.sleep(0.2)
        print("humi level:"+str(humi.get_temp()))
        time.sleep(0.2)
        
        
        
if __name__ == "__main__":
    main()    
        
        