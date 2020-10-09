import math

class Offset:

    def __init__(self, dx=0, dy=0, phi=0):
        self.dx = dx
        self.dy = dy
        self.phi = phi

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)

    def add(self, offset):
        self.dx += offset.dx
        self.dy += offset.dy
        self.phi += offset.phi

    def assign_offset(self,x,y,phi=0):
        w = (self.phi+phi)/(2*math.pi)*360
        rx = round(x * math.cos(w) - y * math.sin(w) + self.dx*100)
        ry = round(x * math.sin(w) + y * math.cos(w) + self.dy*100)
        return rx, ry

