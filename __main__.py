from class_LCD import*
from class_TH import*
from class_FND2 import*
from class_VR import*
from class_LED import*
from threading import Thread

import time
###############################
thread_stop = 0
spi_vr = VR()
lcd = LCD()
th = TempHumi()
fnd_text = FND2()
led = LED()

#text_D = ['BAD']*3
#text_C = ['CLEAN']*5

chr_name = ''
echr_name = ''
dust = 0.0

def fd():
    while True:        
        fnd_text.FND_disp(dust)
        if thread_stop == 1:
            break
def ld():
    while True:
        #time.sleep(0.02)
        if dust < 10:
            lcd.lcd_string(("T:%d  H:%d" % (int(th.get_temp()),int(th.get_humi()))),LCD_LINE_1)        
            lcd.lcd_string(("D:%d   %s" %(int(dust),echr_name)), LCD_LINE_2)
            
        elif 10<= dust <100:
            lcd.lcd_string(("T:%d  H:%d" % (int(th.get_temp()),int(th.get_humi()))),LCD_LINE_1)        
            lcd.lcd_string(("D:%d  %s" %(int(dust),echr_name)), LCD_LINE_2)

        else:
            lcd.lcd_string(("T:%d  H:%d" % (int(th.get_temp()),int(th.get_humi()))),LCD_LINE_1)        
            lcd.lcd_string(("D:%d %s" %(int(dust),echr_name)), LCD_LINE_2)
        if thread_stop == 1:
                    break

#print(th.get_temp())
#print(th.get_humi())

try:
    t1 = Thread(target = fd)
    t2 = Thread(target = ld)
    t1.start()
    t2.start()
    while True:
        #adc_vol[1]=spi_vr.get_vol(int(spi_vr.analog_read(1))) #VR값 받아옴
        dust = spi_vr.analog_read(1)/27.3 #나쁨판별 변수
        #print(dust)
        #print(text_1)
        #print(th.get_temp())
        #print(th.get_humi())
        spi_vr.change_motor(dust)
        #print(dust)
        
        if 0 <= dust < 15:
            chr_name = '좋음'
            echr_name = 'Good' 
            GPIO.output(led_b,GPIO.HIGH)
            GPIO.output(led_r,GPIO.LOW)
            GPIO.output(led_g,GPIO.LOW)
            
        elif 16< dust <50 :
            chr_name = '보통'
            echr_name = 'Normal'
            GPIO.output(led_g,GPIO.HIGH)
            GPIO.output(led_r,GPIO.LOW)
            GPIO.output(led_b,GPIO.LOW)
            
        elif 51 < dust <100:
            chr_name = '나쁨'
            echr_name = 'Bad'
            GPIO.output(led_g,GPIO.HIGH)
            GPIO.output(led_r,GPIO.HIGH)
            GPIO.output(led_b,GPIO.LOW)
            
            
        elif 101 < dust <= 150:
            chr_name = '매우나쁨'
            echr_name = 'Very Bad'
            GPIO.output(led_r,GPIO.HIGH)
            GPIO.output(led_b,GPIO.LOW)
            GPIO.output(led_g,GPIO.LOW)
            #fnd_test.FND_disp(text_B)
        #print(chr_name)
            
        
       #fnd_test.FND_disp(text_B)
       #fnd_test.FND_disp(text_C)
        
       
        #lcd.lcd_string(("%d" % light.readLight1()),LCD_LINE_1)
        #lcd.lcd_string(temp,LCD_LINE_1)
        #lcd.lcd_string(humi,LCD_LINE_2)
        #lcd.lcd_string(spi,LCD_LINE_1)
        #lcd.lcd_byte(0x01,LCD_CMD)

        
                
        
        
finally:
    thread_stop = 1
    t1.join()
    t2.join()
    GPIO.cleanup()
    
