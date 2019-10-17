# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   004-建造者模式-创建电脑.py
@Time    :   2019/10/16 22:53:23
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   通过模拟建造组装电脑展示建造者模式
             在下面几种情况下，与工厂模式相比，建造模式更好：
             1.想要创建一个复杂对象，对象由多个部分组成，且对象的创建要经过多个不同的步骤，这些步骤也许
             还要遵从一定的顺序
             2.要求一个对象能有不同的表现，并希望将对象的构造与表现解耦
             3.想要在某个时间段创建对象，但在稍后的时间点再访问
'''

# here put the import lib
import random
import string

class Computer(object):
    def __init__(self):
        self.serial = None
        self.cpu = None
        self.memory = None
        self.ssd = None
    def __str__(self):
        info = ('\n\n电脑信息如下：',
            'Serial: {}'.format(self.serial),
            'CPU: {} Core'.format(self.cpu),
            'Memory: {} GB'.format(self.memory),
            'SSD: {} GB'.format(self.ssd)
        )
        return '\n'.join(info)

class ComputerBulider(object):
    def __init__(self):
        self.computer = Computer()
    def taken_serial(self):
        print('获取电脑序列号')
        self.computer.serial = ''.join(random.sample(string.ascii_uppercase,2)+random.sample(string.digits,8))
    def build_cpu(self,avalue):
        print('构建CPU')
        self.computer.cpu = avalue
    def build_memory(self,avalue):
        print('构建内存')
        self.computer.memory = avalue
    def build_ssd(self,avalue):
        print('构建ssd盘')
        self.computer.ssd = avalue
    
class HadwareEngineer(object):
    def __init__(self):
        self.builder = None
    def assemble_compute(self,cpu,memory,ssd):
        self.builder = ComputerBulider()
        print('开始组装电脑..')
        [step for step in (
            self.builder.taken_serial(),
            self.builder.build_cpu(cpu),
            self.builder.build_memory(memory),
            self.builder.build_ssd(ssd))]
        print('组装电脑完成..')
    @property
    def computer(self):
        return self.builder.computer

def main():
    engineer = HadwareEngineer()
    engineer.assemble_compute(cpu=2.4,memory=16,ssd=1000)
    computer = engineer.computer  
    print(computer)

if __name__ == "__main__":
    main()
