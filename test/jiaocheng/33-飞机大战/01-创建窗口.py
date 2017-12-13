#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 12 Dec 2017 07:40:33 PM CST

# File Name: 01-创建窗口.py
# Description:

"""

import pygame
import time
def main():
    #创建窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #创建背景图片
    background = pygame.image.load('./feiji/background.png')
    while True:
        screen.blit(background, (0,0))
        pygame.display.update()
        time.sleep(0.02)
if __name__ == '__main__':
    main()

