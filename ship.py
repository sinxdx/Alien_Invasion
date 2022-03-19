import pygame
from bullet import Bullet


class Ship:
    """创建自机，在创建时，需要传入两个参数--自机设置：<class>auto_setting, “屏幕”：<union>screen"""

    def __init__(self, auto_setting, screen):
        """初始化自机"""
        self.screen = screen  # 读入自机图层——这个ship.screen是用来绘制自机用的
        self.screen_rect = screen.get_rect()  # 这个screen_rect是用来计算飞船初始位置的
        self.auto_setting = auto_setting  # 自机的设置，比如速度之类的东西
        '''加载自机图像'''
        self.image = pygame.image.load('material/自机.bmp')
        self.rect = self.image.get_rect()  # 读取自机图像的rect值

        '''初始化自机位置在屏幕底部中央'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom

        '''再创建两个变量，以使得能在飞船的属性center中存储小数值'''
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        '''初始化移动标志为不动'''
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False  # 初始化向右移动标志为False

    def update(self):
        """用于根据移动标志计算并输出飞船的位置"""
        '''下面这部分是计算飞船的位置'''
        if self.moving_left and self.centerx > self.screen_rect.left:  # <union>screen本身就有left这个子成员，传入参数时就有了，直接用
            self.centerx -= self.auto_setting.ship_speed_factor
        if self.moving_right and self.centerx < self.screen_rect.right:
            self.centerx += self.auto_setting.ship_speed_factor
        if self.moving_up and self.centery > 0:
            self.centery -= 1
        if self.moving_down and self.centery < self.screen_rect.bottom:
            self.centery += 1
        '''下面这部分是输出飞船的位置：把上面的计算结果，变量centerx和centery的值放置到self.rect去，然后下面的blitme()使用这两个变量
        来绘制飞船，即可实现飞船位置的输出'''
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitem(self):
        """在指定位置绘制自机"""
        self.screen.blit(self.image, self.rect)