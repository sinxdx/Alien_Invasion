import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对发射子弹进行管理的类"""

    def __init__(self, bullet_setting, bullet_screen, bullet_ship):
        """对子弹进行初始化"""
        '''直接继承Sprite的各种方法'''
        super().__init__()
        self.screen = bullet_screen  # 用于绘制子弹图层

        '''在（0,0）处创建一个表示子弹的矩形，然后再设置其正确的位置（发射时的位置）'''
        self.rect = pygame.Rect(0, 0,  # 子弹矩形左上角的坐标
                                bullet_setting.bullet_width, bullet_setting.bullet_height)  # 子弹矩形的长宽
        self.rect.centerx = bullet_ship.rect.centerx  # 子弹从自机中间发射出
        self.rect.top = bullet_ship.rect.top
        '''存储子弹的y坐标，用于打印不同速度的子弹——x坐标因为不变所以直接就用自己的x了'''
        self.y = float(bullet_ship.rect.centery)
        '''子弹的颜色和速度设置'''
        self.speed_factor = bullet_setting.bullet_speed_factor
        self.color = bullet_setting.bullet_color
        '''子弹的数量限制'''
        self.maxnum = bullet_setting.bullet_maxnum

    def update(self, bullets) -> None:
        """定义向上移动子弹的方法"""
        '''更新储存子弹y坐标的参数'''
        self.y -= self.speed_factor
        '''把储存的y参数赋值给子弹本身'''
        self.rect.y = self.y
        '''若子弹的y已经到达屏幕顶端，则把它从Group()中移除'''
        if self.rect.y <= 0:
            bullets.remove(self)
        '''如果子弹数量超过了最大允许数量，则移除最先发射的那个子弹'''
        if len(bullets) > self.maxnum:
            bullets.remove(self)  # .remove()移除的是Group()里最先的那个

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
