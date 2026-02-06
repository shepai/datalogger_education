import time
import board
import analogio
import busio
import adafruit_mpu6050
import adafruit_dht

#Code to make reading sensors much easier and simpler

class analoguesensor:
    #analog sensor generic class
    def __init__(self,pinNo):
        self.pin = analogio.AnalogIn(pinNo)
    def readPin(self,dt=0.01):
        val=(self.pin.value * 3.3) / 65535
        time.sleep(dt)
        return val

#classes below to make it pleasing to the user
class co2(analoguesensor): 
    def __init__(self,pin):
        super().__init__(pin)

class moisture(analoguesensor): 
    def __init__(self,pin):
        super().__init__(pin)

class light(analoguesensor): 
    def __init__(self,pin):
        super().__init__(pin)

class sound(analoguesensor): 
    def __init__(self,pin):
        super().__init__(pin)

#gyro read 
class MPU:
    def __init__(self,sda,scl):
        i2c = busio.I2C(scl, sda)  # Uses default I2C pins
        self.mpu = adafruit_mpu6050.MPU6050(i2c)
    def getGyro(self):
        return self.mpu.gyro
    def getAcc(self):
        return self.mpu.acceleration
    def getTemp(self):
        return self.mpu.temperature
    
class humidity:
    def __init__(self,pin):
        self.dht =  adafruit_dht.DHT11(pin)
    def getTemp(self):
        return self.dht.temperature
    def getHumidity(self):
        return self.dht.humidity