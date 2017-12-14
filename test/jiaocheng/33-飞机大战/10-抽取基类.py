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
import random

class Base(object):
    def __init__(self,screen_tmp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_tmp
        self.image = pygame.image.load(image_name)

class Baseplane(Base):
    def __init__(self,screen_tmp, x, y, image_name):
        Base.__init__(self,screen_tmp, x, y, image_name)    
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)

class Heroplane(Baseplane):
    def __init__(self, screen_tmp):
        Baseplane.__init__(self,screen_tmp,210,650,'./feiji/hero1.png')

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
            
class Enemyplane(Baseplane):
    def __init__(self,screen_tmp):
        Baseplane.__init__(self,screen_tmp,0,0,'./feiji/enemy0.png')
        self.direction = "right"
        
    def move(self):
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10

        if self.x < 0:
            self.direction = "right"
        elif self.x > 430:
            self.direction == "left"

    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 18:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class Basebullet(Base):
    def display(self):
        self.screen.blit(self.image, (self.x,self.y))

class Bullet(Basebullet):
    def __init__(self, screen_tmp, x, y):
        Basebullet.__init__(self, screen_tmp, x+40, y-20, './feiji/bullet.png')

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y < 0:
            return True
        return False

class EnemyBullet(Basebullet):
    def __init__(self, screen_tmp, x, y):
        Basebullet.__init__(self, screen_tmp, x+25, y+40, './feiji/bullet1.png')

    def move(self):
        self.y += 10

    def judge(self):
        if self.y > 852:
            return True
        return False

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
    #创建敌机对象
    enemy = Enemyplane(screen)
    while True:
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)
if __name__ == '__main__':
    main()
