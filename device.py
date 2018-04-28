import serial, serial.tools.list_ports

class Device():
    '''
    指纹识别器的操作，包括连接，指令发送，数据接收
    '''
    def __init__(self,port_name, baud_rate ):
        self.port_name = port_name
        self.baud_rate = baud_rate
        #连接串口
        try:
            self.port = serial.Serial(self.port_name, self.baud_rate, timeout = 0.5) 
        except Exception as e:
            pass
        
                
    def recive_data(self):
        #接收串口消息
        while True:
            data = self.port.readline().decode()
            if data :
                self.message = data
                return self.message
               
    def send_cmd(self, cmd):
        #发送命令
        if self.port.isOpen():
            self.port.write(cmd)
            
    def get_finger_id(self):
        #获取指纹ID
        self.send_cmd(b"get_finger_id")
        id = self.recive_data()
        return id
       
                
    def add_fingerprint(self):
        #添加指纹
        self.send_cmd(b"add_fingerprint")
          
