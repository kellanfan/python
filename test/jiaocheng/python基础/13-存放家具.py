#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 25 Oct 2017 07:56:55 PM CST

# File Name: 13-存放家具.py
# Description: 将家具放到房子里面，计算房子的剩余面积，和放入家具的名字

"""

#定义一个类：家
class Home:
    #定义Home类，属性有面积，户型，位置，剩余面积，存放家具
    #定义init方法，这个是初始化属性的
    def __init__(self, home_area, home_info, home_addr):
        self.area = home_area
        self.info = home_info
        self.addr = home_addr
        self.left_area = home_area
        self.contain_items = []
    def __str__(self):
        return "我家地址是%s,户型是%s,面积是%d,剩余面积是%d,添加的家具有%s"%(self.addr,self.info,self.area,self.left_area,str(self.contain_items))
    def add_item(self,item): 
    #这里的self指向myhome对象，而下面myhome.add_item(bed1)，是item指向bed1对象
        self.left_area -= item.get_area()
        self.contain_items.append(item.get_name())
#定义床类
class Bed:
    def __init__(self,bed_name,bed_area):
        self.name = bed_name
        self.area = bed_area
    def __str__(self):
        return "添加的家具是%s,它的面积是%d"%(self.name, self.area)
    def get_name(self):
        return self.name
    def get_area(self):
        return self.area
myhome = Home(300,"五室一厅","北京市")
print(myhome)

bed1 = Bed("席梦思",4)
print(bed1)
myhome.add_item(bed1)
print(myhome)
