import serial #pyserial
import io
import Kamera


class Plotter:


    def __init__(self):
        self.ser = None
        self.sio = None
        self.kamera = None


    def __del__(self):
        x, y = self.read_pos()
        print("X = {}, Y = {}".format(x, y))
        self.ser.write(b'\x1b.[ZF6;')  # switch offline
        self.ser.close()
        print("COM prot closed")

    def rs232_init(self, port):
        self.ser = serial.Serial()
        self.ser.baudrate = 19200
        self.ser.port = port # 'COM4'
        self.ser.parity = 'N'
        self.ser.stopbits = 1
        self.ser.bytesize = 8
        self.ser.timeout = 1
        self.ser.xonxoff = 0
        self.ser.rtscts = 1

        self.ser.open()

        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

        print("ser.is_open --> " + str(self.ser.is_open) + " one " + self.ser.name)

        self.ser.write(b'\x1b.[ZF5;') # switch online

        self.ser.write(b'OC;')  # position abfragen
        tmp = self.read_rs232()
        x, y = self.read_pos()
        print("X = {}, Y = {}".format(x, y))

    def kamera_init(self,device_index):
        self.kamera= Kamera.Kamera(device_index)

    def read_rs232(self):
        buffer = ""
        while True:
            oneByte = self.ser.read(1)
            if oneByte == b"\r":  # method should returns bytes
                return buffer
            else:
                buffer += oneByte.decode("ascii")

    def read_pos(self):
        self.ser.write(b'OC;')  # position abfragen
        tmp = self.read_rs232()
        x = tmp[0:7]
        y = tmp[14:21]
        return int(x), int(y)

    def move(self, x, y):
        command = 'PU' + str(x*100) + ',' + str(y*100) + ';'
        self.ser.write(command.encode())
        x, y = self.read_pos()
        print("X = {}, Y = {}".format(x, y))

    def move_kamera(self,x ,y):
        self.move(x+self.kamera.offset_x, y+self.kamera.offset_y)

    def bild_erstellen(self):
        return self.kamera.get_image()

    def kreis_gravieren(self,x,y,r):
        self.ser.write(b'PA;')
        self.ser.write(b'XX13,12,0;SP1;SD0;EG1;VU100.0')
        self.ser.write(b'PW0,0,0,0;LL5;ML5;EL0;VS100;AS3,3;LF20000;QU2;')

        self.move(x, y)
        self.ser.write("CI{}".format(r*100).encode())
        self.move(x, y)



def einrichten():
    # test mauel einrichten
    pt = Plotter()
    pt.kamera_init(1)
    pt.rs232_init("COM3")
    pt.kreis_gravieren(85,200,3)
    pt.move_kamera(85,200)
    pt.kamera.manuel_einrichten()

def move():
    pt = Plotter()
    pt.move_kamera(0,0)

if __name__ == '__main__':
    einrichten()