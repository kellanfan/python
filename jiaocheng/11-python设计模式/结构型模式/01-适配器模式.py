# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   01-适配器模式.py
@Time    :   2019/12/17 20:13:15
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
# 适配器模式，帮助我们实现两个不兼容的接口之间的兼容。遵从开放/封闭原则。
# 开放/封闭原则是面向对象设计的基本原则之一，声明一个软件实体应该对扩展是开放的，对修改是封闭的

from external import Synthesizer, Human

class Computer(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'execute a program.'

class Adapter(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods) 

    def __str__(self):
        return str(self.obj)

def main():
    objects = [Computer('IBM')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play))) #这里是把其他类的相应的方法指定到execute方法上
    human = Human('kellan')
    objects.append(Adapter(human, dict(execute=human.speak)))
    print(objects)
    for i in objects:
        #print(i.name)
        print('{} {}'.format(str(i), i.execute()))


if __name__ == "__main__":
    main()
