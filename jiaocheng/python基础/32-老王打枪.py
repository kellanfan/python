#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 06 Dec 2017 05:03:36 PM CST

# File Name: 32-老王打枪.py
# Description: 一个对象要引用另一个对象，需要在这个对象创建一个属性指向另一个对象的引用

"""
class Person(object):
    def __init__(self,name):
        self.name = name
        self.gun = None #保存枪对象的引用
        self.hp = 100

    def az_zidan(self, danjia_tmp, zidan_tmp):
        danjia_tmp.baocun_zidan(zidan_tmp)

    def az_danjia(self, gun_tmp, danjia_tmp):
        gun_tmp.baocun_danjia(danjia_tmp)

    def naqiang(self, gun_tmp):
        self.gun = gun_tmp

    def __str__(self):
        if self.gun:
            return "%s的血量为%d,他有枪,枪的信息：%s"%(self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为%d,他没有枪"%(self.name, self.hp)
            else:
                return "%s挂了..."%self.name

    def kou_banji(self, diren):
        '''让枪去打敌人'''
        self.gun.fire(diren)

    def diaoxue(self,shanghai):
        self.hp -= shanghai

class Gun(object):
    def __init__(self,name):
        self.name = name
        self.danjia = None #记录弹夹的有无

    def __str__(self):
        if self.danjia:
           return "%s有弹夹，%s"%(self.name, self.danjia)
        else:
           return "%s没有弹夹"%self.name

    def baocun_danjia(self, danjia_tmp):
        self.danjia = danjia_tmp

    def fire(self,diren):
        '''枪从弹夹中获取一发子弹，让后让子弹击中敌人'''
        #先从弹夹中取子弹，
        zidan_tmp = self.danjia.qu_zidan()
        #让子弹去伤害敌人
        if zidan_tmp:
            zidan_tmp.dazhong(diren)
    

class Danjia(object):
    def __init__(self, max_count):
        self.max_count = max_count #弹夹存储最大的子弹数
        self.zidan_list = []#记录所有子弹的引用

    def __str__(self):
        if self.zidan_list:
            return "弹夹的信息：%d/%d" %(len(self.zidan_list), self.max_count)
        else:
            return "无子弹"

    def baocun_zidan(self, zidan_tmp):
        self.zidan_list.append(zidan_tmp)

    def qu_zidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None
class Zidan(object):
    def __init__(self,shanghai):
        self.shanghai = shanghai #子弹的伤害

    def dazhong(self,diren):
        '''子弹伤害敌人，让敌人掉血'''
        #敌人.掉血(子弹的伤害)
        diren.diaoxue(self.shanghai)

def main():
    '''控制整个程序'''
#1. 创建老王
    laowang = Person('老王')
#2. 创建枪
    ak47 = Gun('AK47')
#3. 创建弹夹
    dan_jia = Danjia(20)
#4. 创建一些子弹
    #5. 老王把子弹安装到弹夹
    #老王.安装子弹（弹夹，子弹）
    for i in range(18):
        zi_dan = Zidan(10)
        laowang.az_zidan(dan_jia, zi_dan)
#6. 老王把弹夹安装到枪上
    laowang.az_danjia(ak47, dan_jia)

#测试
#print ak47
#7. 老王拿枪
    laowang.naqiang(ak47)
#test
    print laowang
#8. 创建敌人
    diren = Person('老宋')
    print diren
#9. 老王开枪打敌人
    for i in range(5):
        laowang.kou_banji(diren)
    print diren

if __name__ == '__main__':
    main()
