class Handler:
    x = 0
    y = 0
    mg = False
    mm = []
    shifton = False
    ctrlon = False
    @staticmethod
    def handle(socket, connection, address):
        try:
            while True:
                data = connection.recv(socket.size).decode()
                if data:
                    pass
                else:
                    break
                Thread(target=socket.handler,args=(data,)).start()
        except Exception as e:
            print(str(e))
        finally:
            print("CLOSING CONNECTION")
            connection.close()

    @staticmethod
    def handleVolume(data):
        n = int(data)
        if n <= 0:
            data = -96
        n = n/100
        data = -69+69*n
        if data > 0:
            data = 0
        volume.SetMasterVolumeLevel(int(data), None)
        
    @staticmethod
    def handleYoutube(data):
        if data[0] == '0':
            YT()
        if data[0] == '1':
            YT.inst.get('https://www.youtube.com')
    
    @staticmethod
    def handleMouseMove(data):
        offset_x = int(data.split('|')[0])
        offset_y = int(data.split('|')[1])
        move(offset_x,offset_y)
    
    @staticmethod
    def handleMouseClick(data):
        
        if data == '0':
            leftPress()
        if data == '1':
            leftRelease()
        if data == '2':
            rightPress()
        if data == '3':
            rightRelease()
        if data == '4':
            os.system(r"C:\WINDOWS\system32\Magnify.exe")
            #Thread(target=os.system,args=(r"C:\WINDOWS\system32\Magnify.exe",)).start()
        if data == '5':
            PressKey(0xDB + 1024)
            PressKey(0x01)
            ReleaseKey(0xDB + 1024)
            ReleaseKey(0x01)
        if data == '6':
            leftPress()
            time.sleep(0.001)
            leftRelease()
        if data == '7':
            PressKey(0xDB + 1024)
            PressKey(0x0D)
            ReleaseKey(0xDB + 1024)
            ReleaseKey(0x0D)
        if data == '8':
            PressKey(0xDB + 1024)
            PressKey(0x0C)
            ReleaseKey(0xDB + 1024)
            ReleaseKey(0x0C)
    
    @staticmethod
    def handleKeyboard(data):
 
        try:
            key = ANDR_CODES[data]
            keyhex = keyboard_key_mapping[key]
        except:
            return
        
        if key == 'SHIFT':
            if Handler.shifton == True:
                PressKey(keyboard_key_mapping['LEFT_CTRL'])
                Handler.ctrlon = True
            else:
                Handler.shifton = True
                PressKey(keyhex)
        else:
            PressKey(keyhex)
            ReleaseKey(keyhex) 
            
        if key != 'SHIFT':
            if Handler.shifton == True:
                Handler.shifton = False
                ReleaseKey(0x2A)
            if Handler.ctrlon == True:
                Handler.ctrlon = False
                ReleaseKey(keyboard_key_mapping['LEFT_CTRL'])