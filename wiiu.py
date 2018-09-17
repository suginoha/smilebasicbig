#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

pygame.init()
window_size = (100, 100)
screen = pygame.display.set_mode(window_size)
img_map = pygame.image.load('prg02.jpg')

gx = 0
gy = 0

def decode8():
    global gx
    global gy
    a = 0

    for i in range(8):
        col = img_map.get_at((gx, gy))
        if col.r>200:
            a=a+pow(2,(7-i))
        gx=gx+1
        if gx==854:
            gx=0
            gy=gy+1
    return a

def imgtotext():
    st=""
    for x in range(854*30):
        s=decode8()*0x100+decode8()
        if s>0:
            st=st+chr(s)
        #st=st+hex(decode8()*0x100+decode8())+" "
    f = open('text.txt', 'w')
    f.write(st)
    f.close()

imgtotext()

pygame.quit()
quit()
