from net.tcpclient import TcpClient

class RelayEthernet:
    def __init__(self):
        # Default Relay Settings
        self.address              = "192.168.1.4"
        self.port                 = 3000
        # Functions
        self.id_query             = 0x10 # query
        self.id_one_off           = 0x11 # one off
        self.id_one_on            = 0x12 # one on
        self.id_all               = 0x13 # all
        # Checksum is appended to final array
        #                             start, class,   ID,     ,     , index, index ] chk
        self.relay_16_template    = [  0x58,  0x01, 0x11, 0x00, 0x00,  0x00,  0x00 ]

    def setAddress(self, address):
        self.address = address

    def setPort(self, port):
        self.port = int(port)


    def enableAll(self):
        localArray = [ x for x in self.relay_16_template ]
        localArray[2] = self.id_all
        localArray[5] = 0xFF
        localArray[6] = 0xFF
        localArray.append(self.getCheckSum(localArray))

        tcpClient = TcpClient()
        tcpClient.connect(self.address, self.port)
        if tcpClient.write(localArray) == len(localArray):
            return True
        return False

    def disableAll(self):
        localArray = [ x for x in self.relay_16_template ]
        localArray[2] = self.id_all
        localArray.append(self.getCheckSum(localArray))

        tcpClient = TcpClient()
        tcpClient.connect(self.address, self.port)
        if tcpClient.write(localArray) == len(localArray):
            return True
        return False

    def enable(self, index):
        localArray = [ x for x in self.relay_16_template ]
        localArray[2] = self.id_one_on
        localArray[6] = index
        localArray.append(self.getCheckSum(localArray))

        tcpClient = TcpClient()
        tcpClient.connect(self.address, self.port)
        if tcpClient.write(localArray) == len(localArray):
            return True
        return False

    def disable(self, index):
        localArray = [ x for x in self.relay_16_template ]
        localArray[2] = self.id_one_off
        localArray[6] = index
        localArray.append(self.getCheckSum(localArray))

        tcpClient = TcpClient()
        tcpClient.connect(self.address, self.port)
        if tcpClient.write(localArray) == len(localArray):
            return True
        return False

    def getCheckSum(self, byteArray):
        return sum(byteArray) & 0xFF



