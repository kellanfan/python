# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   056-画五角星.py
@Time    :   2019/07/25 01:06:16
@Author  :   Kellan Fan
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   这里给了一个可以画出五星红旗的方法，但是我并没有准确的设计方法，所以不敢擅自画五星红旗。
            如果谁有标准的设计方法，可以基于此代码画出五星红旗，比心。
'''

# here put the import lib

import turtle
import time
'''
turtle.pensize(2) #笔的线条粗细
turtle.pencolor('yellow') #笔的颜色
turtle.fillcolor('red') #空白的填充色

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144) #向右转动144度

turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150,-120) #移动到要写Done这几个字的位置
turtle.color('blue')
turtle.write('Done',font=('Arial',40,'normal'))
time.sleep(2)
'''
class Wjx(object):
    '''
        创建五角星
    '''
    def __init__(self,lenth,startpoint=[],angle=0,pensize=2,pencolor='yellow',fillcolor='yellow'):
        '''
            @lenth 五角星的大小
            @startpoint  五角星的位置
            @angle  五角星的倾斜角度（顺时针倾斜）
            @pensize 笔的粗细
            @pencolor 笔的颜色
            @fillcolor 填充色
        '''
        self.lenth = lenth
        self.startpoint = startpoint
        self.angle = angle
        turtle.pensize(pensize)
        turtle.pencolor(pencolor)
        turtle.fillcolor(fillcolor)
    def skip(self):
        turtle.penup()
        turtle.goto(self.startpoint)
        turtle.pendown()
    def __call__(self):
        if self.startpoint:
            self.skip()
        turtle.begin_fill()
        self.arch()
        turtle.end_fill()
    def arch(self):
        if self.angle:
            turtle.right(self.angle)
        for _ in range(5):
            turtle.forward(self.lenth)
            turtle.right(144)
        

if __name__ == "__main__":
    turtle.screensize(800,600, "red")
    a = Wjx(200)
    b = Wjx(100,[100,200],-20)
    a()
    b()