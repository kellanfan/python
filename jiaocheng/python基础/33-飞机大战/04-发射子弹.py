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

class Heroplane(object):
    def __init__(self,screen_tmp):
        self.x = 210
        self.y = 650
        self.screen = screen_tmp
        self.image = pygame.image.load('./feiji/hero1.png')
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
            
class Bullet(object):
    def __init__(self, screen_tmp, x, y):
        self.x = x+40
        self.y = y-20
        self.screen = screen_tmp
        self.image = pygame.image.load('./feiji/bullet.png')

    def display(self):
        self.screen.blit(self.image, (self.x,self.y))

    def move(self):
        self.y -= 10

def key_control(hero_tmp):
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
                hero_tmp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_tmp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_tmp.fire()

def main():
    #创建窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #创建背景图片
    background = pygame.image.load('./feiji/background.png')
    #创建玩家飞机对象
    hero = Heroplane(screen)
    while True:
        screen.blit(background, (0,0))
        hero.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)
if __name__ == '__main__':
    main()

