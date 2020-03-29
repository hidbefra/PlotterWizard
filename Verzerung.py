import numpy as np
from scipy import interpolate #install scipy
import cv2
import math


quadrat = np.array(
    [
    [0,60],
    [30,60],
    [60,60],
    [60,30],
    [60,0],
    [60,-30],
    [60,-60],
    [30,-60],
    [0,-60],
    [-30,-60],
    [-60,-60],
    [-60,-30],
    [-60,0],
    [-60,30],
    [-60,60],
    [-30,60]
])*3

height = 800
width = 800

dot_grid = []


image = np.zeros((height, width,3), np.uint8)

# bild erstellen
r = 200
px = len(quadrat)*5
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
n=32
for i in range(n):
    rb = 400
    w = math.pi *2/n*i+math.pi/4
    x = int(math.cos(w)*rb+width/2)
    y = int(math.sin(w)*rb+height/2)
    points.append([x,y])
    values_x.append(0)
    values_y.append(0)
    image = cv2.circle(image, (x, y), 2, (0, 255, 255), -1)

# stützpunkte erstellen
n = len(quadrat)
for i in range(int(n)):
    w = (math.pi/2-math.pi *2 / int(n)*(i))
    x = int(math.cos(w)*r+width/2)
    y = int(math.sin(w)*r+height/2)
    nx = int(quadrat[i][0]+width/2)
    ny = int(quadrat[i][1]+width/2)
    points.append([x,y])
    image = cv2.circle(image, (x, y), 5, (255, 255, 255), -1)

    dx = nx-x
    dy = ny-y

    values_x.append(dx)
    values_y.append(dy)

    image = cv2.circle(image, (x + dx, y + dy), 5, (0, 0, 255), -1)

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

cv2.imshow("", image)
cv2.waitKey(0)