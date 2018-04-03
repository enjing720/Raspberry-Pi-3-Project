import smbus2 as smbus
import time

bus1= smbus.SMBus(1)
addr1= 0x20
config_port = 0x06
out_port = 0x02
num_list=[]

null = 0x00
#data1 = (0xFC, 0x60, 0xDA, 0XF2, 0X66, 0xB6, 0x3E, 0xE0, 0XFE, 0xF6)
data_t=(0xFE, 0xEE, 0xFC, 0x9C, 0x1C, 0x9E, 0xEE, 0xEC,0xFC, 0x60, 0x0A, 0xE0, 0x66)
digit = (0x7F, 0XBF, 0xDF, 0xEF, 0XF7, 0xFB)

class FND:
    def __init__(self):
        #self.data1=(0xFC, 0x60, 0xDA, 0XF2, 0X66, 0xB6, 0x3E, 0xE0, 0XFE, 0xF6)
        #self.data_t =(0xFE, 0xEE, 0xFC)
        #self.digit = (0x7F, 0XBF, 0xDF, 0xEF, 0XF7, 0xFB)
        pass

    def FND_break(self):
        bus1.write_word_data(addr1, out_port, 0x00FF)
        time.sleep(0.001)
        
        
    def FND_disp(self, num):
        number=[' ']*6
        
        for i in range(0,len(num),1):
            
            if num[i] == 'BAD':
                number[i + (len(number) - len(num))] = num[i]
                
            elif num[i] == 'CLEAN':
                number[i] = num[i]
                        
        
        for i in range (0,len(number)):
            if number[i] == ' ':
                out_disp = null << 8 | digit[i]
                bus1.write_word_data(addr1, out_port, out_disp)
                time.sleep(0.002)
            
            elif number[i] =='CLEAN':
                out_disp =  data_t[i+3] << 8 | digit[i]
                bus1.write_word_data(addr1, out_port, out_disp)
                time.sleep(0.002)
            
            elif number[i] == 'BAD':
                out_disp =  data_t[i-3] << 8 | digit[i]
                bus1.write_word_data(addr1, out_port, out_disp)
                time.sleep(0.002)
               
            
            else:
                out_disp =  data1[int(number[i])] << 8 | digit[i]
                bus1.write_word_data(addr1, out_port, out_disp)
                time.sleep(0.002)
            
        
            
        bus1.write_word_data(addr1, out_port, 0x00FF) 

