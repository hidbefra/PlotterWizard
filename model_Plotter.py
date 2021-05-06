import serial #pyserial
import io
import Kamera
import concurrent.futures
import asyncio
import time
import model_Settings
from status_text import status_text
from part_count import part_count
import PlotterWizard
from enum import Enum


class Plotter:


    def __init__(self, settings: model_Settings.Settings):
        self.ser = serial.Serial()
        self.sio = None
        # self.kamera = None
        self.hpgl_code = ""
        self.thread: concurrent.futures.Future = None
        self.plotter_running = False
        self.plotter_online = False
        self.init_rs232(settings)


    def __del__(self):
        # x, y = self.read_pos()
        # print("X = {}, Y = {}".format(x, y))
        # self.ser.write(b'\x1b.[ZF6;')  # switch offline
        self.ser.close()
        status_text.add_line_to_status_text("COM prot closed")


    def init_rs232(self, settings: model_Settings.Settings):
        # self.ser = serial.Serial()
        self.ser = None
        self.ser = serial.Serial()
        self.ser.baudrate = settings.setings["com_port"]["baudrate"]
        self.ser.port = settings.setings["com_port"]["RS232port"]
        self.ser.parity = settings.setings["com_port"]["parity"]
        self.ser.stopbits = settings.setings["com_port"]["stopbits"]
        self.ser.bytesize = settings.setings["com_port"]["bytesize"]
        self.ser.timeout = settings.setings["com_port"]["timeout"]
        self.ser.xonxoff = settings.setings["com_port"]["xonxoff"]
        self.ser.rtscts = settings.setings["com_port"]["rtscts"]

        try:
            self.ser.open()

            self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

            status_text.add_line_to_status_text("ser.is_open --> " + str(self.ser.is_open) + " one " + self.ser.name)
        except:
            status_text.add_line_to_status_text("Port " + self.ser.name + " kannn nicht geöfnet werden")


    def reinit_rs232(self, settings: model_Settings.Settings):
        self.ser.close()
        status_text.add_line_to_status_text("COM prot closed")
        time.sleep(1)
        self.init_rs232(settings)

    def init_plotter(self):
        self.ser.write(b'\x1b.[ZF5;')  # switch online

        self.ser.write(b'OC;')  # position abfragen
        tmp = self.read_rs232()
        x, y = self.read_pos()
        status_text.add_line_to_status_text("X = {}, Y = {}".format(x, y))

    def kamera_init(self,device_index):
        self.kamera= Kamera.Kamera(device_index)

    def read_rs232(self):
        status_text.add_line_to_status_text("rs232 read")
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
        status_text.add_line_to_status_text("X = {}, Y = {}".format(x, y))

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
        if not self.plotter_running:
            status_text.add_line_to_status_text("starte prozess")
            self.plotter_running = True
            thread_pool = concurrent.futures.ThreadPoolExecutor()
            self.thread = thread_pool.submit(self._prozess_run, self.hpgl_code) # start thread
            # self._prozess_run(self.hpgl_code)
        else:
            status_text.add_line_to_status_text("läuft schon")
        pass

    def prozess_stop(self):

        if self.plotter_running:
            self.plotter_running = False
            time.sleep(1)
            while(not self.thread.done()):
                self.ser.cancel_write()
                self.ser.cancel_read()
                status_text.add_line_to_status_text("cancel rs232 write")
                time.sleep(1)
            status_text.add_line_to_status_text("gestopt")

        else:
            status_text.add_line_to_status_text("läuft gar nicht")
        pass

    def _prozess_run(self, hpgl_code):
        while (self.plotter_running):
            self.write_rs232(hpgl_code)

            self.ser.write(b'JB1337;') # use Job Echo um ende des Programs zu markieren

            buffer = "" # auf antwort vom Plotter warten
            while (self.plotter_running):
                oneByte = self.ser.read(1)
                if oneByte == b"\r":  # method should returns bytes
                    break
                else:
                    # print(oneByte.decode("ascii"))
                    buffer += oneByte.decode("ascii")
            part_count.add_part()
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