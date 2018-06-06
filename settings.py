# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:22:55 2018

@author: 黄蒙蒙
设置
"""
class Settings():
    '''存储该游戏的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (230,230,230)
        #飞船速度的设置
        self.ship_speed_factor = 1.5