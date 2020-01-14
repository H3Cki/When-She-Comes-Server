import ctypes
import time
from ctypes import windll, Structure, c_long, byref


PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]
class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]
class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]
class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]
class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]
    

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
    
   
    
    
class DirectInput:
    
    ANDR_CODES = {
    "29": 'a',
    "30": 'b',
    "31": 'c',
    "32": 'd',
    "33": 'e',
    "34": 'f',
    "35": 'g',
    "36": 'h',
    "37": 'i',
    "38": 'j',
    "39": 'k',
    "40": 'l',
    "41": 'm',
    "42": 'n',
    "43": 'o',
    "44": 'p',
    "45": 'q',
    "46": 'r',
    "47": 's',
    "48": 't',
    "49": 'u',
    "50": 'v',
    "51": 'w',
    "52": 'x',
    "53": 'y',
    "54": 'z',
    "55": 'COMMA',
    "56": 'PERIOD',
    "69": 'DASH',
    "59": 'SHIFT',
    "62": 'SPACE',
    "66": 'ENTER',
    "67": 'BACKSPACE',
    "7 ": '0',
    "8 ": '1',
    "9 ": '2',
    "10": '3',
    "11": '4',
    "12": '5',
    "13": '6',
    "14": '7',
    "15": '8',
    "16": '9'}

    keyboard_key_mapping = {
    'ESCAPE': 0x01,
    'F1': 0x3B,
    'F2': 0x3C,
    'F3': 0x3D,
    'F4': 0x3E,
    'F5': 0x3F,
    'F6': 0x40,
    'F7': 0x41,
    'F8': 0x42,
    'F9': 0x43,
    'F10': 0x44,
    'F11': 0x57,
    'F12': 0x58,
    'BACKTICK': 0x29,
    '1': 0x02,
    '2': 0x03,
    '3': 0x04,
    '4': 0x05,
    '5': 0x06,
    '6': 0x07,
    '7': 0x08,
    '8': 0x09,
    '9': 0x0A,
    '0': 0x0B,
    'MINUS': 0x0C,
    'DASH': 0x0C,
    'EQUALS': 0x0D,
    'BACKSPACE': 0x0E,
    'INSERT': 0xD2 + 1024,
    'HOME': 0xC7 + 1024,
    'PAGE_UP': 0xC9 + 1024,
    'NUMLOCK': 0x45,
    'NUMPAD_DIVIDE': 0xB5 + 1024,
    'NUMPAD_SLASH': 0xB5 + 1024,
    'NUMPAD_MULTIPLY': 0x37,
    'NUMPAD_STAR': 0x37,
    'NUMPAD_SUBTRACT': 0x4A,
    'NUMPAD_DASH': 0x4A,
    'TAB': 0x0F,
    'q': 0x10,
    'w': 0x11,
    'e': 0x12,
    'r': 0x13,
    't': 0x14,
    'y': 0x15,
    'u': 0x16,
    'i': 0x17,
    'o': 0x18,
    'p': 0x19,
    'LEFT_BRACKET': 0x1A,
    'RIGHT_BRACKET': 0x1B,
    'BACKSLASH': 0x2B,
    'DELETE': 0xD3 + 1024,
    'END': 0xCF + 1024,
    'PAGE_DOWN': 0xD1 + 1024,
    'NUMPAD_7': 0x47,
    'NUMPAD_8': 0x48,
    'NUMPAD_9': 0x49,
    'NUMPAD_ADD': 0x4E,
    'NUMPAD_PLUS': 0x4E,
    'CAPSLOCK': 0x3A,
    'a': 0x1E,
    's': 0x1F,
    'd': 0x20,
    'f': 0x21,
    'g': 0x22,
    'h': 0x23,
    'j': 0x24,
    'k': 0x25,
    'l': 0x26,
    'SEMICOLON': 0x27,
    'APOSTROPHE': 0x28,
    'no': 0x1C,
    'ENTER': 0x1C,
    'SHIFT': 0x2A,
    'z': 0x2C,
    'x': 0x2D,
    'c': 0x2E,
    'v': 0x2F,
    'b': 0x30,
    'n': 0x31,
    'm': 0x32,
    'COMMA': 0x33,
    'PERIOD': 0x34,
    'SLASH': 0x35,
    'RIGHT_SHIFT': 0x36,
    'UP': 0xC8 + 1024,
    'LEFT_CTRL': 0x1D,
    'LEFT_SUPER': 0xDB + 1024,
    'LEFT_WINDOWS': 0xDB + 1024,
    'LEFT_ALT': 0x38,
    'SPACE': 0x39,
    'RIGHT_ALT': 0xB8 + 1024,
    'RIGHT_SUPER': 0xDC + 1024,
    'RIGHT_WINDOWS': 0xDC + 1024,
    'APP_MENU': 0xDD + 1024,
    'RIGHT_CTRL': 0x9D + 1024,
    'LEFT': 0xCB + 1024,
    'DOWN': 0xD0 + 1024,
    'RIGHT': 0xCD + 1024,
    }
    
    class Keyboard:
        shifton = False
        ctrlon = False
        alton = False
        
        
    class Mouse:
        hold = False
        x = 0
        y = 0


    @staticmethod
    def move(args):
        split = args.split("|")
        x = int(split[0])
        y = int(split[1])
        extra = ctypes.c_ulong(0)     
        ii_ = Input_I()
        ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
        
        
    @staticmethod
    def leftPress():
        DirectInput.Mouse.hold = True
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
        
        
    @staticmethod
    def leftRelease():
        DirectInput.Mouse.hold = False
        extra = ctypes.c_ulong(0) 
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
        
        
    @staticmethod
    def rightPress():
        extra = ctypes.c_ulong(0) 
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
        
        
    @staticmethod
    def rightRelease():
        extra = ctypes.c_ulong(0) 
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0010, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
        
    
    @staticmethod
    def clickLeft():
        if DirectInput.Mouse.hold != True:
            DirectInput.leftPress()
        DirectInput.leftRelease()
    
   
    @staticmethod
    def clickRight():
       DirectInput.rightPress()
       DirectInput.rightRelease()    
        
        
    @staticmethod    
    def pressKey(hexKeyCode):
        extra = ctypes.c_ulong(0) 
        if hexKeyCode >= 1024:
            key = hexKeyCode - 1024
            flags = 0x0008 | 0x0001
        else:
            key = hexKeyCode
            flags = 0x0008
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
        
        
    @staticmethod
    def releaseKey(hexKeyCode):
        extra = ctypes.c_ulong(0) 
        if hexKeyCode >= 1024:
            key = hexKeyCode - 1024
            flags = 0x0008 | 0x0001 | 0x0002
        else:
            key = hexKeyCode
            flags = 0x0008 | 0x0002
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
        
    
        
    @staticmethod
    def writeKey(hexKeyCode):
        DirectInput.pressKey(hexKeyCode)
        DirectInput.releaseKey(hexKeyCode)
        
        
    @staticmethod
    def getKey(keyCode):
        print(f"GETTING {keyCode} ({type(keyCode)})")
        key = ANDR_CODES[keyCode]
        return keyboard_key_mapping[key]
    
    @staticmethod
    def getMousePos():
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return (pt.x, pt.y) 