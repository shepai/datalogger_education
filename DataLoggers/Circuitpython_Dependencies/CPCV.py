import board
import busio
import time
import digitalio
import ulab.numpy as np

class AI_cam:
    def __init__(self,camera,cropW=0,cropH=0):
        self.camera=camera
        self.w=cropW
        self.h=cropH
    def takePic(self):
        buf = bytearray(2 * self.camera.width * self.camera.height)
        self.camera.capture(buf)
        a = np.frombuffer(buf, dtype=np.uint16)
        return a,buf
    def convert_byte_array_to_image(self, byte_array):
        # Check if the byte array length matches the expected size
        width=self.camera.width
        height=self.camera.height
        if len(byte_array) != width * height * 2 and len(byte_array) != width * height:
            raise ValueError("Byte array size does not match the expected image size")
        
        # Create an empty numpy array for the image
        #imageR = np.zeros((height, width), dtype=np.uint8) #[[[0,0,0] for j in range(camera.width)] for i in range(camera.height)]#np.zeros((height, width), dtype=np.uint8)
        #imageB = np.zeros((height, width), dtype=np.uint8)
        #imageG = np.zeros((height, width), dtype=np.uint8)
        gray=np.zeros((height-self.h, width-self.w), dtype=np.uint8)
        # Process each pixel
        for i,y in enumerate(range(self.h//2,height-self.h//2)):
            for j,x in enumerate(range(self.w//2,width-self.w//2)):
                index = (y * width + x) * 2
                # Extract the RGB565 pixel
                pixel = byte_array[index] << 8 | byte_array[index + 1]
                
                # Convert RGB565 to RGB888
                r = (pixel >> 11) & 0x1F
                g = (pixel >> 5) & 0x3F
                b = pixel & 0x1F
                
                # Scale to 8-bit values
                r = (r * 255) // 31
                g = (g * 255) // 63
                b = (b * 255) // 31
                
                # Assign to the image array
                Clinear = 0.2126 * r + 0.7152 * g + 0.0722 * b
                #imageR[y, x] = r#[r, g, b]
                #imageG[y, x] = g
                #imageB[y, x] = b
                gray[i,j]=Clinear
        return gray#imageR,imageG,imageB
    def show(self):
        p,a=self.takePic()
        p=self.convert_byte_array_to_image(a)
        print("Gray=[",end="")
        for i in range(self.camera.height):
            print("[",end="")
            for j in range(self.camera.width):
                print(p[i][j],",",end="")
            print("],")
        print("]")
    def snap(self):
        p,a=self.takePic()
        p=self.convert_byte_array_to_image(a)
        return p
    def compress(self,image, new_size):
        original_height, original_width = image.shape[:2]
        new_height, new_width = new_size
        scaled_image = np.zeros((new_height, new_width))

        row_scale = original_height / new_height
        col_scale = original_width / new_width

        for i in range(new_height):
            for j in range(new_width):
                row_start = int(i * row_scale)
                row_end = int((i + 1) * row_scale)
                col_start = int(j * col_scale)
                col_end = int((j + 1) * col_scale)
                scaled_image[i, j] = np.mean(image[row_start:row_end, col_start:col_end])

        return scaled_image
