# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:44:52 2019

@author: Dmitry
"""
import itertools
import matplotlib.pyplot as plt
import math
import random

def incircle(A, B, C): 
    ab = math.hypot(B[0] - A[0], B[1] - A[1])
    bc = math.hypot(B[0] - C[0], B[1] - C[1])
    ca = math.hypot(C[0] - A[0], C[1] - A[1])

    if (ab + bc <= ca) or (ab + ca <= bc) or (ca + bc <= ab):
        flag = 0
    else:
        flag = 1
        
    return flag
    
def checkPoint(subset, point):
    
    a = (subset[0][0] - point[0]) * (subset[1][1] - subset[0][1])
    a -= (subset[1][0] - subset[0][0]) * (subset[0][1] - point[1])
    b = (subset[1][0] - point[0]) * (subset[2][1] - subset[1][1])
    b -= (subset[2][0] - subset[1][0]) * (subset[1][1] - point[1])
    c = (subset[2][0] - point[0]) * (subset[0][1] - subset[2][1])
    c -= (subset[0][0] - subset[2][0]) * (subset[2][1] - point[1])
    
    if (a > 0 and b > 0 and c > 0) or (a < 0 and b < 0 and c < 0):
        '''
        print('Принадлежит')
        print(point)
        '''
        flag = 1
    else:
        '''
        print('Не принадлежит')
        '''
        flag = 0
        
    return flag

def checkMn1Modif(subset, usedPoint, mn1Modif):
    flagMn1 = 0
    for point in mn1Modif:
        if point not in usedPoint:
            if point != subset[0] and point != subset[1]:
                if point != subset[2] and checkPoint(subset, point) == 1:
                    usedPoint.append(point)
                    flagMn1 += 1
                
    return flagMn1
    
def checkMn2Modif(subset, usedPoint, mn2Modif):
    flagMn2 = 0
    for point in mn2Modif:
        if point not in usedPoint:
            if point != subset[0] and point != subset[1]:
                if point != subset[2] and checkPoint(subset, point) == 1:
                    usedPoint.append(point)
                    flagMn2 += 1
                
    return flagMn2

def inputXcoordinates(subset):
    xTriangle = []
    
    xTriangle.append(subset[0][1])
    xTriangle.append(subset[1][1])
    xTriangle.append(subset[2][1])
    xTriangle.append(subset[0][1])
    
    return xTriangle

def inputYcoordinates(subset):
    yTriangle = []
                        
    yTriangle.append(subset[0][0])
    yTriangle.append(subset[1][0])
    yTriangle.append(subset[2][0])
    yTriangle.append(subset[0][0])
    
    return yTriangle

def buildPointsMn1(mn1Modif):
    for point in mn1Modif:
        plt.plot(point[0], point[1], marker = 'o', color = 'r')
        
def buildPointsMn2(mn2Modif, subset):
    for point in mn2Modif:
        if point != subset[0] and point != subset[1] and point != subset[2]:
            if point not in mn1Modif:
                plt.plot(point[0], point[1], marker = 'o', color = 'b')
    
def buildtriangle(subset):
    plt.plot(inputYcoordinates(subset), 
             inputXcoordinates(subset), marker = 'o', color = 'g')
    
'''
Для ручного ввода координат

'''

'''
mn1Modif = [[1, 3], [5, 6], [2, 0], [1, -0.5], [3, -5], [1, 3]]
mn2Modif = [[-2, -1], [3, 4], [1, 2], [0, 0], [1, 8], [5, 6], [3, 0]]
'''


mn1Modif = [[random.randint(0, 10) for j in range(3)] for i in range(5)]
mn2Modif = [[random.randint(0, 10) for j in range(3)] for i in range(5)]

flagWork = 1
p = 1
for L in range(0, len(mn1Modif)):
    print(mn1Modif[L])
    for i in mn1Modif:
        if i != mn1Modif[]:
            print(i[0])
            print(L[0])
            if ((i[0] - L[0]) ** 2 + (i[1] - L[1]) ** 2) ** 0.5:
                pass
        














                    
