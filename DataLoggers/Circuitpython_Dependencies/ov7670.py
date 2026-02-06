import board
import busio
from adafruit_ov7670 import OV7670
from adafruit_ov7670 import (  # pylint: disable=unused-import
    OV7670,
    OV7670_SIZE_DIV2,
    OV7670_SIZE_DIV4,
    OV7670_SIZE_DIV8,
    OV7670_COLOR_YUV,
    OV7670_TEST_PATTERN_COLOR_BAR_FADE,
    OV7670_COLOR_RGB,
)
# Initialize the camera
bus = busio.I2C(board.GP9, board.GP8)
camera = OV7670(
    bus,
    data_pins=[board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19],
    clock=board.GP11,
    vsync=board.GP7,
    href=board.GP21,
    mclk=board.GP20,
    #shutdown=board.D39,
    reset=board.GP10,
)
camera.colorspace = OV7670_COLOR_RGB
camera.size=OV7670_SIZE_DIV4
