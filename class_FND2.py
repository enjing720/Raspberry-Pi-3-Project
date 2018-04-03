import smbus2 as smbus
import time

bus1= smbus.SMBus(1)
addr1= 0x20
config_port = 0x06
out_port = 0x02
num_list=[]

data_D=(0xFC, 0x60, 0x0A, 0xE0, 0x66)
data_C=(0x9C, 0x1C, 0x9E, 0xEE, 0xEC)
digit = (0x7F, 0XBF, 0xDF, 0xEF, 0XF7, 0xFB)

class FND2:
    def __init__(self):
        pass
    
    def FND_break(self):
        bus1.write_word_data(addr1, out_port, 0x00FF)
        time.sleep(0.002)
        
    def FND_disp(self,num):
        if num <50: #clean
            for i in range (0,5):
                self.out_disp =  data_C[i] << 8 | digit[i]
                bus1.write_word_data(addr1, out_port, self.out_disp)
                time.sleep(0.002)
                self.FND_break()
        else:
            for i in range (0,5):
                self.out_disp =  data_D[i] << 8 | digit[i+1]
                bus1.write_word_data(addr1, out_port, self.out_disp)
                time.sleep(0.002)
                self.FND_break()
                

        
        
    
