from bullet import Bullet
import pygame


class BulletDebug(Bullet):
    """用于调试的子弹，修改了子弹的宽度，使其能一发清除掉所有飞船"""
    def __init__(self, setting, screen, ship):
        """重写子弹的宽"""
        Bullet.__init__(self, setting, screen, ship)
        self.rect = pygame.Rect(0, 0,  # 子弹矩形左上角的坐标
                                setting.bullet_debug_width, setting.bullet_height)  # 子弹矩形的长宽
        self.rect.centerx = ship.rect.centerx  # 子弹从自机中间发射出
        self.rect.top = ship.rect.top
