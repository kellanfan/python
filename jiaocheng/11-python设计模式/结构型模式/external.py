# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   01-external.py
@Time    :   2019/12/17 22:24:37
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

class Synthesizer(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song.'

class Human(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'say hello'