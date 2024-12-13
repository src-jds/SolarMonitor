import logging
from waveshare_epd import epd2in13_V4
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

class display:
    refreshIntervalSec = 180
    partialRefreshLimit = 10

    def __init__(self):
        self.state = "imported"
        self.batteryVoltage = 0
        self.batteryCurrent = 0
        self.panelVoltage = 0
        self.panelCurrent = 0
        self.uptimeHours = 0
        self.partialRefreshCount = 0
        self.refreshTimerSec = 0 

    def init(self):
        logging.info("Initialising E-Paper display")
        self.epd = epd2in13_V4.EPD()
        self.epd.init()
        self.epd.Clear(0xFF)
        self.image = Image.new('1', (self.epd.height, self.epd.width), 255)
        self.graphics = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype("./pic/Font.ttc", 24)
        self.state = "initialised"

    def showText(self, message):
        self.message = message
        self.graphics.text((50,50),self.message,font=self.font,fill = 0)
        self.epd.display(self.epd.getbuffer(self.image))
        #self.image.clear()

    def checkRefreshTimer(self):
        pass

    def updateBatteryVoltage(self, voltage):
        self.batteryVoltage = voltage

    def updateBatteryCurrent(self, current):
        self.batteryCurrent = current

    def updatePanelVoltage(self, voltage):
        self.panelVoltage = voltage

    def updatePanelCurent(self, current):
        self.panelCurrent = current

    def close(self):
        self.epd.Clear(0xFF)
        self.epd.close()
