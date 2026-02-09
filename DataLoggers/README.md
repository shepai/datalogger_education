## Setting up

You will need a Raspberry Pi Pico, a computer with USB connection and to download <a href="https://thonny.org/">Thonny IDE</a>. 

Once you have all of these, you may need to reflash the Raspberry Pi Pico if it is new. To do this hold down the bbotsel button and then connect the usb to the pico and computeer. Be sure to keep the button pressed in this time. Once it is connected it should come up with the boot menu. Drag the most <a href="https://circuitpython.org/board/raspberry_pi_pico/">recent download of circuitpython</a> for Pico into the folder. 

See <a href="https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython">this tutorial</a> for more detail.

Once all set up you will need to upload the libary dependencies to the board. The files can be found under ```/Circuitpython_Dependencies``` copy and paste the contents of this folder into ```lib/``` on the pico. If there are compatibility issues with any of these libraries it might be because your circuitpython flash is more up to date than these libraries. If so you will need to install the latest ones from <a href="https://circuitpython.org/libraries">here</a>.

## Wiring
To wire up your data logger you will need to select sensors you want to read from, SD card reader (optional), breadboard, buttons and Pico. 

First begin by placing each component you will be using on the breadboard so that the lines do not cross, we will use jumper wires to connect the electronics. 

### SD card
The SD card is optional, though if you do not use an SD card the device can not be connected to Thonny while you gather data, otherwise you will get an error stating:
```[bash]
Traceback (most recent call last): File "<stdin>", 
line 48, in <module> File "<stdin>", 
line 20, in __init__ 
RuntimeError: Cannot remount path when visible via USB.
```
If this happens, simply unplug the device and make sure your code is running on boot by saving it as ```code.py``` so that as soon as power goes into the device, it runs your program. If you are using a USB plugged into your laptop and it keeps reconnecting automatically to Thonny, close Thonny before gathering data and plugging the device in. Remember that the device has limited data sorage, so be sure to keep backing up the files on your PC. 

If you do have an SD card then it is wired as follows: 

<p align="center">
  <img src="../Assets/Screenshot from 2026-02-06 17-15-32.png" width="70%">
</p>

| SD Pin | Pico Pin |
|-------|-------|
| MOSI | GP3 |
| MISO | GP4 |
| GND | GND |
| 5V/3.3 | See table below |
| SCK | GP2 |
| CS | GP1 |

Different SD readers may have different power requriements. Below is a table that explains what should be wired to what.

| SD card holder | Power requirement | Pin on Pico |
|------|-------|-------|
| ![Demo1](../Assets/Screenshot%20from%202026-02-06%2017-16-28.png) | 5V | VBUS |
| ![Demo2](../Assets/Screenshot%20from%202026-02-06%2017-16-35.png) | 3.3V | 3.3 |


### MPU6050 sensor 
The MPU6050 is a gyroscope, accelerometer and temperature sensor. We will be using this sensor to gather human movement datasets that we can later classify. 

<p align="center">
  <img src="../Assets/MPU6050-Gyroscope-Accelerometer-Raspberry-Pi-Pico.png"
       width="30%"
       style="transform: rotate(90deg);">
</p>

| MPU6050 Pin | Pico Pin |
|-------|-------|
| GND | GND |
| VCC | 3.3 |
| SDA | GP20 |
| SCL | GP21 |

### Push button
We include the use of a push button to allow you to stop and start recording from the sensor to your file.

<p align="center">
  <img src="../Assets/Screenshot 2026-02-07 093117.png"
       width="30%"
       style="transform: rotate(90deg);">
</p>


### LED
The LED is our user interface. On smart phones we have screens that tell us what is going on, but if we are trying to be low cost, low power consuming, we can use an LED to let us know if we are recording data or not. 

<p align="center">
  <img src="../Assets/Screenshot 2026-02-07 092959.png" width="70%">
</p>

Notice that the LED has one pin slightly longer than the other. The longer pin is our positive, and shorter pin the negative. Connect the shorter pin to the GND on the Pico, and longer pin to GP28

## Coding
Once the libraries are uploaded under the \lib folder, you can upload the ```demo code.py``` file to the pico and rename it as code.py which will allow it to run on boot. 
The coding is all done for you, but if you are feeling confident have a play around to try understand it. 

## Gathering your dataset

Now you have a device that can record multiple datasets. The device should look something like this. When you give it power it is ready to go, if you press the button then the LED should come on, and when you press it again it goes off. While the LED is on, the device is recording. Your first file will be called log0.csv, then second one log1.csv and so on. Remember what you are doing for each file, for you will need to label it when you make classifiers later on. 

<p align="center">
  <img src="../Assets/46090.jpg" width="70%">
</p>

Ideally if you have an external phone charger, you can power the device on the move with the USB. Otherwise keep it connected to your laptop and carefully perform different tasks while holding the data logger device. 