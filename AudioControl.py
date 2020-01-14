from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL



class AudioController:
    @staticmethod
    def initialize():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        AudioController.volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        
    @staticmethod
    def setVolume(vol):
        n = int(vol)
        if n <= 0:
            vol = -96
        n = n/100
        vol = -69+69*n
        if vol > 0:
            vol = 0
        AudioController.volume.SetMasterVolumeLevel(vol, None)
        
        
AudioController.initialize()