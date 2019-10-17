# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   02-抽象工厂模式.py
@Time    :   2019/10/16 21:09:17
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   抽象工厂模式示例
             工厂模式和抽象工厂可以用于：
             1.想要追踪对象的创建 
             2.想要将对象的创建和使用解耦
             3.想要优化应用的性能和资源占用
             工厂模式的实现是一个不属于任何类的单一函数负责单一种类的对象的创建
             抽象工厂的实现是同属于单个类的许多个工厂方法用于创建一系列种类的相关对象
'''

# here put the import lib
class Frog(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def meet_with(self,obstacle):
        '''
            遇到障碍物的输出
        '''
        print('{}! The Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))

class Bug(object):
    def __str__(self):
        return 'a bug'
    def action(self):
        '''
            障碍物与主角接触后的动作
        '''
        return 'eats it'

class FrogWorld(object):
    '''
        抽象工厂，主要职责是创建游戏的主角和障碍物，区分创建方法并使其名字通用，这让我们可以动态的改变当前激活
        的工厂
    '''
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t------Frog World------'
    def make_role(self):
        return Frog(self.player_name)
    def make_obstacle(self):
        return Bug()

class Hero(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def meet_with(self,obstacle):
        print('The hero {} encounters {} and {}!'.format(self, obstacle, obstacle.action()))

class Ork(object):
    def __str__(self):
        return 'a ork'
    def action(self):
        return 'kill it!'

class HeroWorld(object):
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t------Hero World------'
    def make_role(self):
        return Hero(self.player_name)
    def make_obstacle(self):
        return Ork()

class GameEnv(object):
    def __init__(self, factory):
        self.lead = factory.make_role()
        self.obstacle = factory.make_obstacle()
    def play(self):
        self.lead.meet_with(self.obstacle)

def valid_age(name):
    try:
        age = input('Welcome {}! How old are you?'.format(name))
        age = int(age)
    except:
        print('Age {} is invalid, please input again..'.format(age))
        return (False, age)
    else:
        return (True, age)
def main():
    name = input('What is your name?')
    vaild_input = False
    while not vaild_input:
        vaild_input, age = valid_age(name)
    game = FrogWorld if age<18 else HeroWorld
    env = GameEnv(game(name))
    env.play()
if __name__ == "__main__":
    main()