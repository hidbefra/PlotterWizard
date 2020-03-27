import numpy as np
from scipy import interpolate
import cv2
import math
import random


height = 1000
width = 1000

dot_grid = []


image = np.zeros((height, width,3), np.uint8)

# bild erstellen
r = 300
px = 50
for i in range(px):
    w = math.pi *2/px*i
    x=int(math.cos(w)*r+width/2)
    y=int(math.sin(w)*r+height/2)
    dot_grid.append([x,y])
    image = cv2.circle(image, (x, y), 1, (255, 255, 255), -1)

for i in range(px):
    w = math.pi *2/px*i
    x=int(math.cos(w)*r*1.2+width/2)
    y=int(math.sin(w)*r*1.2+height/2)
    dot_grid.append([x,y])
    image = cv2.circle(image, (x, y), 1, (255, 255, 255), -1)

for i in range(px):
    w = math.pi *2/px*i
    x=int(math.cos(w)*r*0.8+width/2)
    y=int(math.sin(w)*r*0.8+height/2)
    dot_grid.append([x,y])
    image = cv2.circle(image, (x, y), 1, (255, 255, 255), -1)


grid_x, grid_y = np.mgrid[0:height, 0:width]

points = []
values_x = []
values_y = []

# äusere Begrenzung erstellen
begrenzung = height*2**(1/2)*0.5*0.9
for i in range(100):
    w = math.pi * 2 / 100*i+math.pi/4
    x = math.cos(w)*begrenzung+width/2
    y = math.sin(w)*begrenzung+height/2
    points.append([x,y])
    image = cv2.circle(image, (int(x), int(y)), 2, (0, 255, 255), -1)
    values_x.append(0)
    values_y.append(0)


# stützpunkte erstellen
for i in range(int(px/10)):
    w = math.pi *2/int(px/10)*i
    x = math.cos(w)*r+width/2
    y = math.sin(w)*r+height/2
    points.append([x,y])
    image = cv2.circle(image, (int(x), int(y)), 5, (255, 255, 255), -1)

    dx = (0.5 - random.random()) * 100
    dy = (0.5 - random.random()) * 100

    values_x.append(dx)
    values_y.append(dy)

    image = cv2.circle(image, (int(x + dx), int(y + dy)), 5, (0, 0, 255), -1)

# für x und y verzerungsproviel lösen
grid_zx = interpolate.griddata(points, values_x, (grid_x, grid_y), method='cubic')
grid_zy = interpolate.griddata(points, values_y, (grid_x, grid_y), method='cubic')
grid_zx = np.nan_to_num(grid_zx)
grid_zy = np.nan_to_num(grid_zy)

# zeichnen der verzerung
for pnt in dot_grid:
    x = pnt[0]
    y = pnt[1]
    dx = int(grid_zx[x, y])
    dy = int(grid_zy[x, y])
    print(dx)
    image = cv2.circle(image, (x + dx, y + dy), 1, (0, 0, 255), -1)

cv2.imwrite('test.png', image)
cv2.imshow("", image)
cv2.waitKey(0)
