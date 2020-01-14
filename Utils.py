import os
from DirectInput import DirectInput as DI

class Utils:
    @staticmethod
    def enableZoom():
        os.system(r"C:\WINDOWS\system32\Magnify.exe")
    @staticmethod
    def disableZoom():
        DI.pressKey(0xDB + 1024)
        DI.pressKey(0x01)
        DI.releaseKey(0xDB + 1024)
        DI.releaseKey(0x01)
    @staticmethod
    def zoomIn():
        DI.pressKey(0xDB + 1024)
        DI.pressKey(0x0D)
        DI.releaseKey(0xDB + 1024)
        DI.releaseKey(0x0D)
    @staticmethod
    def zoomOut():
        DI.pressKey(0xDB + 1024)
        DI.pressKey(0x0C)
        DI.releaseKey(0xDB + 1024)
        DI.releaseKey(0x0C)