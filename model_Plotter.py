import serial #pyserial
import io
import Kamera
import concurrent.futures
import asyncio
import time
from enum import Enum


class Plotter:


    def __init__(self):
        self.ser = serial.Serial()
        self.sio = None
        # self.kamera = None
        self.hpgl_code = ""
        self.thread: concurrent.futures.Future = None
        self.plotter_running = False
        self.plotter_online = False
        self.init_rs232('COM3')


    def __del__(self):
        # x, y = self.read_pos()
        # print("X = {}, Y = {}".format(x, y))
        # self.ser.write(b'\x1b.[ZF6;')  # switch offline
        self.ser.close()
        print("COM prot closed")


    def init_rs232(self, port):
        # self.ser = serial.Serial()
        self.ser.baudrate = 19200
        self.ser.port = port  # 'COM4'
        self.ser.parity = 'N'
        self.ser.stopbits = 1
        self.ser.bytesize = 8
        self.ser.timeout = 1
        self.ser.xonxoff = 0
        self.ser.rtscts = 1

        self.ser.open()

        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

        print("ser.is_open --> " + str(self.ser.is_open) + " one " + self.ser.name)

    def init_plotter(self):
        self.ser.write(b'\x1b.[ZF5;')  # switch online

        self.ser.write(b'OC;')  # position abfragen
        tmp = self.read_rs232()
        x, y = self.read_pos()
        print("X = {}, Y = {}".format(x, y))

    def kamera_init(self,device_index):
        self.kamera= Kamera.Kamera(device_index)

    def read_rs232(self):
        print("rs232 read")
        buffer = ""
        while True:
            oneByte = self.ser.read(1)
            if oneByte == b"\r":  # method should returns bytes
                return buffer
            else:
                # print(oneByte.decode("ascii"))
                buffer += oneByte.decode("ascii")

    def write_rs232(self,data):
        self.ser.write(data.encode())

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

    def prozess_init(self, hpgl):
        self.hpgl_code = hpgl

    def prozess_start(self):
        # self._prozess_run()
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     f1 = executor.submit(self._prozess_run)

        # task = asyncio.create_task(self._prozess_run())

        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     f1 = executor.submit(_prozess_run)
        # pass
        if not self.plotter_running:
            print("starte prozess")
            self.plotter_running = True
            thread_pool = concurrent.futures.ThreadPoolExecutor()
            self.thread = thread_pool.submit(self._prozess_run, self.hpgl_code) # start thread
            # self._prozess_run(self.hpgl_code)
        else:
            print("läuft schon")
        pass

    def prozess_stop(self):

        if self.plotter_running:
            self.plotter_running = False
            time.sleep(1)
            while(not self.thread.done()):
                self.ser.cancel_write()
                self.ser.cancel_read()
                print("cancel rs232 write")
                time.sleep(1)
            print("gestopt")

        else:
            print("läuft gar nicht")
        pass

    def _prozess_run(self, hpgl_code):
        while (self.plotter_running):
            self.write_rs232(hpgl_code)

            buffer = ""
            while (self.plotter_running):
                oneByte = self.ser.read(1)
                if oneByte == b"\r":  # method should returns bytes
                    break
                else:
                    # print(oneByte.decode("ascii"))
                    buffer += oneByte.decode("ascii")
            # self.read_pos() # scheint die einfachtste Lösung zu sein um herauszufiden ob das Programm durchgelaufen ist
            print(buffer)
        print("prozess abgebrochen")
        pass




def einrichten():
    # test mauel einrichten
    pt = Plotter()
    pt.kamera_init(1)
    pt.init_rs232("COM3")
    pt.kreis_gravieren(85,200,3)
    # pt.move_kamera(85,200)
    pt.kamera.manuel_einrichten()

def move():
    pt = Plotter()
    pt.move_kamera(0,0)

if __name__ == '__main__':
    einrichten()