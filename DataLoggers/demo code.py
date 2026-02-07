#import the data logging lib
import busio
import digitalio
import board
from dataloggerCP import datalogger
import adafruit_mpu6050
import time 

#set up the pins 
spi = busio.SPI(board.GP2, board.GP3, board.GP4)
cs = digitalio.DigitalInOut(board.GP1)
i2c = board.I2C(board.GP20,board.GP21) #might need to flip it
btn=digitalio.DigitalInOut(board.GP18)
btn.direction=digitalio.Direction.INPUT
btn.pull=digitalio.Pull.UP
LED=digitalio.DigitalInOut(board.GP18)
LED.direction=digitalio.Direction.OUTPUT
#set up the sensor
mpu = adafruit_mpu6050.MPU6050(i2c)
logger=datalogger(spi,cs)
#read line function from the sensor
def read():
   xa,ya,za=mpu.acceleration
   xg,yg,zg=mpu.gyro 
   return str(xa)+","+str(ya)+","+str(za)+","+str(xg)+","+str(yg)+","+str(zg)+"\n"

toggle=False
LED.value=False
num=0
#loop
while 1: 
   if not btn.value:
      toggle = not toggle
      LED.value = not LED
      if logger.opened: #save the file
         logger.close()
      else: #if no file is opened
         logger.create_file("log"+str(num)+".csv")
         num+=1
   if toggle:
     dataline=read()
     logger.write_data(dataline)
   time.sleep(0.2)
#when toggeled on record, when toggled off stop