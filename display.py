import logging
from waveshare_epd import epd2in13_V4
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

class display:
    def __init__(self);
        display = epd2in13_V4.EPD()
        logging.info("init and Clear")
        display.init()
        display.Clear(0xFF)

    def drawText(self, message);
       self.message = message

