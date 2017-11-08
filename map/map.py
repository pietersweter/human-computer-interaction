#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gradients as grd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
#import math as m
import math

def drawMap(_map, fileName):
    fig = plt.figure()
    plt.imshow(_map)
    plt.show()
    fig.savefig(fileName + ".pdf")

def loadCoordinates(fileName):
    with open(fileName) as file:
        _map = file.read().splitlines()
    _map = [i.split(' ') for i in _map]
    _height = int(_map[0][0])
    _width = int(_map[0][1])
    _distance = int(_map[0][2])
    del _map[0]
    return _map, _height, _width, _distance

def colorMap(mapData, colorData):
    for i in range (0, len(mapData)):
        for j in range(0, len(mapData[i])):
            #print(_map[i][j])
            #print(mapData[i][j])
            try:
                if float(mapData[i][j]) < 60:
                    colorData[i][j][0] = 0.7
                    colorData[i][j][1] = 0.5
                    colorData[i][j][2] = 0
                else:
                    colorData[i][j] = 0
            except:
                print(mapData[i][j])

    return colorData

if __name__ == '__main__':
    _map, _height, _width, _distance = loadCoordinates("big.dem")
    _color = np.zeros((_height, _width, 3), dtype=np.float32)
    _color = colorMap(_map, _color)
    tmp = np.zeros((5, 3, 3), dtype=np.float32)
    tmp[0][2][0] = 1
    drawMap(tmp, "map")
    #mapaVector = vectorShading(mapa, mapHeight, mapWidth, distance)
    #drawMap(mapaVector,"vectorMap.pdf")
    plt.close()