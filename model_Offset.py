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
        w = (self.phi+phi)/360*(2*math.pi)
        tx = x + self.dx*100
        ty = y + self.dy*100
        rx = round(tx * math.cos(w) - ty * math.sin(w))
        ry = round(tx * math.sin(w) + ty * math.cos(w))
        return rx, ry

