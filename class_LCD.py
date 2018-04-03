import RPi.GPIO as GPIO
import time

LCD_RS=23
LCD_E=26
LCD_D4=17
LCD_D5=18
LCD_D6=27
LCD_D7=22
cnt = 0
LCD_WIDTH = 20  #Maximum characters per line
LCD_CHR = True
LCD_CMD= False

LCD_LINE_1=0x80  #LCD RAM adress for the 1st line
LCD_LINE_2=0xC0  #LCD RAM adress for the 2nd line

#Timing constants
E_PULSE=0.0005
E_DELAY=0.0005


class LCD:  
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)        #Use BCM GPIO number

        GPIO.setup(LCD_E, GPIO.OUT)   #E
        GPIO.setup(LCD_RS, GPIO.OUT)  #RS
        GPIO.setup(LCD_D4, GPIO.OUT)  #DB4
        GPIO.setup(LCD_D5, GPIO.OUT)  #DB5
        GPIO.setup(LCD_D6, GPIO.OUT)  #DB6
        GPIO.setup(LCD_D7, GPIO.OUT)  #DB7
        #In                
        self.lcd_byte(0x33, LCD_CMD)
        self.lcd_byte(0x32, LCD_CMD)
        self.lcd_byte(0x06, LCD_CMD)
        self.lcd_byte(0x0C, LCD_CMD)
        self.lcd_byte(0x028, LCD_CMD)
        self.lcd_byte(0x01, LCD_CMD)
        time.sleep(E_DELAY)
         
        
        
    def lcd_cntl(type):
        
        if type == "center":
            
            if cnt == 0:
                self.lcd_byte(0x0B,LCD_CMD)
                cnt=1
            else:
                self.lcd_byte(0x0f,LCD_CMD)
                cnt=0
      
#--------------------------------------------------#

    def lcd_init(self):
        #Inintial display
        pass

    #--------------------------------------------------#

    def lcd_byte(self,bits,mode):    
        #send byte to data pins
        #bits = data
        #mode = True for character
        #       False for command
        
        GPIO.output(LCD_RS, mode)
        
    #--------------------------------------------------#
        
    #def lcd_byte(bits,mode):   
        #High bits
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        
        if bits & 0x10 == 0x10:
            GPIO.output(LCD_D4,True)
        if bits & 0x20 == 0x20:
            GPIO.output(LCD_D5, True)
        if bits & 0x40 == 0x40:
            GPIO.output(LCD_D6, True)
        if bits & 0x80 == 0x80:
            GPIO.output(LCD_D7, True)
        #toggle 'Enable' pin    
        self.lcd_toggle_enable()
        
        #LOW bits
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        
        if bits & 0x01 == 0x01:
            GPIO.output(LCD_D4,True)
        if bits & 0x02 == 0x02:
            GPIO.output(LCD_D5, True)
        if bits & 0x04 == 0x04:
            GPIO.output(LCD_D6, True)
        if bits & 0x08 == 0x08:
            GPIO.output(LCD_D7, True)
        #toggle 'Enable' pin    
        self.lcd_toggle_enable()
        
        
    def lcd_toggle_enable(self):
        #toggle enable
        time.sleep(E_DELAY)
        GPIO.output(LCD_E, True)
        time.sleep(E_PULSE)
        time.sleep(E_DELAY)
        GPIO.output(LCD_E, False)
        time.sleep(E_DELAY)    

    #--------------------------------------------------#

    def lcd_string(self,message,line):
        message = message.ljust(LCD_WIDTH," ")
        #message = message.rjust(LCD_WIDTH," ")
        #message = message.center(LCD_WIDTH," ")
        self.lcd_byte(line, LCD_CMD)
        for i in range(len(message)):
            self.lcd_byte(ord(message[i]),LCD_CHR)
        
#def main():
#    while True:
#        lcd_string("Rasbperry Pi", LCD_LINE_1)
#        time.sleep(0.5)
     
                
#        if __name__ == "__main__":
 #           main()
