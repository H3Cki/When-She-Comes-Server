from DirectInput import DirectInput as DI
from AudioControl import AudioController as AC
from Utils import Utils
from threading import Thread
import inspect
import re
import socket
import time
HEADER_SIZE = 32
'''
DATA FORMAT
"HEADER....16DATA"
HEADER: [len|funcname]
'''
class Handler(DI, AC, Utils):
    @staticmethod
    def handle(connection,address):
        got_header = False
        got_msg = False
        try:
            while True:
                if not got_header:
                    header = connection.recv(HEADER_SIZE)
                if header != b'':
                    got_header = True
                    
                if got_header:
                    header = header.decode()
                    header = re.sub(" ","",header)
                    hs = header.split("|")
                    exp_len = int(hs[0])
                    func_name = hs[1]
                    
                    message = connection.recv(exp_len).decode()
                    if message != b'':
                        func = Handler.getMethodByName(func_name)
                        if message:
                            thr = Thread(target=func,args=(message,))
                        else:
                            thr = Thread(target=func)
                        thr.start()
                        got_header = False
                        got_msg = False
                time.sleep(0.005)
        except Exception as e:
            print(str(e))
        finally:
            print("CLOSING CONNECTION")
            connection.close()


    @staticmethod
    def getMethodByName(name):
        #print(f'FINDING METHOD')
        mtds = inspect.getmembers(Handler, predicate=inspect.isfunction)
        for method in mtds:
            if method[0] == name:
                #print(f'found method: {method[0]}')
                return method[1]
        return None
    
    
    @staticmethod
    def handleKeyboard(data):
        #print(f"HANDLING {data} ({type(data)})")
        try:
            key = Handler.ANDR_CODES[data]
            #print(f"KEY {key}")
            keyhex = Handler.keyboard_key_mapping[key]
            #print(f"KEYXEX {keyhex}")
        except:
            return

        if key == 'SHIFT':
            if Handler.Keyboard.shifton == True:
                Handler.pressKey(Handler.keyboard_key_mapping['RIGHT_ALT'])
                Handler.Keyboard.alton = True
            else:
                Handler.Keyboard.shifton = True
                Handler.pressKey(keyhex)
        else:
            Handler.pressKey(keyhex)
            Handler.releaseKey(keyhex) 

        if key != 'SHIFT':
            if Handler.Keyboard.shifton == True:
                Handler.Keyboard.shifton = False
                Handler.releaseKey(0x2A)
        if Handler.Keyboard.alton == True:
            Handler.Keyboard.alton = False
            Handler.releaseKey(Handler.keyboard_key_mapping['RIGHT_ALT'])
                           
class Server:
    def __init__(self,ip,port):
        self.address = (ip,port)
        self.ip = ip
        self.port = port
    
    def start(self):
        print("STARTING SERVER")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)
        
        self.socket.listen(1)
        while True:
            print("ACCEPTING")
            conn, adr = self.socket.accept()
            Thread(target=Handler.handle,args=(conn,adr)).start()
            
            
def main():
    Server("192.168.1.2",1338).start()

main()