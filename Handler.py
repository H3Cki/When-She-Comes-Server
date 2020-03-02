class Handler:
    x = 0
    y = 0
    mg = False
    mm = []
    shifton = False
    ctrlon = False


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
    def handleMouseMove(data):
        offset_x = int(data.split('|')[0])
        offset_y = int(data.split('|')[1])
        move(offset_x,offset_y)
    
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