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
from pygame.locals import *
def main():
    #创建窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #创建背景图片
    background = pygame.image.load('./feiji/background.png')
    #创建玩家飞机图片
    hero = pygame.image.load('./feiji/hero1.png')
    x = 210
    y = 650
    while True:
        screen.blit(background, (0,0))
        screen.blit(hero, (x,y))
        pygame.display.update()
        #获取事件，比如按键等
        for event in pygame.event.get():
            #判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            #判断是否是按下了键
            elif event.type == KEYDOWN:
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x-=5
                #检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x+=5
                #检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
        time.sleep(0.01)
if __name__ == '__main__':
    main()

