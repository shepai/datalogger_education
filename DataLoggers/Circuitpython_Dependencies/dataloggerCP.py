import digitalio
import board
import busio
import sdcardio
import storage
import os
import time
from sensors import *

class datalogger:
    def __init__(self,spi=None,cs=None):
        self.mode=""
        try:
            sdcard = sdcardio.SDCard(spi, cs)
            self.vfs = storage.VfsFat(sdcard)
            storage.mount(self.vfs, "/sd")
            print("successful mount")
            self.mode="/sd/"
        except:
            print("No sd card found... using local storage")
            storage.remount("/", readonly=False)
            self.mode="/"
        self.opened=0
        #set up sd and file
    def create_file(self,filename):
        self.file=open(self.mode+filename,"w")
        self.opened=1
    def write_data(self,data):
        if self.isSpace():
            try:
                self.file.write(data)
            except:
                print("Could not write") #you could also consider putting errors or LED flashes here
        #if there is space
        #write data in the chosen format
    def isSpace(self):
        stats = self.vfs.statvfs(self.mode)
        total_space=stats[2]*stats[1]
        free_space = stats[3] * stats[1]
        used_space = total_space-free_space
        if used_space/(1024**3)<14: #space exists
            return 1
        return 0
        #check how much space there is
    def close(self):
        self.opened=0
        self.file.close()
        #close and save the file

