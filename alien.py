import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个敌机的类"""

    def __init__(self, setting, screen) -> None:
        """

        :rtype: object
        """
        super().__init__()
        self.setting = setting
        self.screen = screen

        '''加载外星人图像，设置rect属性'''
        self.image = pygame.image.load('material/敌机.bmp')
        self.rect = self.image.get_rect()

        '''敌机的初始位置，在屏幕的左上角'''
        self.rect.x = 0  # rect的x,y指的是敌机左上角的那个点
        self.rect.y = 0

        '''储存敌机的小数位置'''
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        '''碰壁信号'''
        self.edge = False
        '''前进信号'''
        self.move_signal:int = 1

    def update(self):
        """更新敌机"""

        def edge():
            """检查敌机是否碰壁"""
            if self.rect.x > self.setting.screen_width - self.setting.screen_reserve_space \
                    or self.rect.x < 0:
                self.edge = True
            else:
                self.edge = False

        def directory(ud='', lr=''):
            """用于更改敌机前进的方向"""
            if lr:
                if lr == -1:  # 向左前进
                    self.x -= self.setting.alien_speed_factor
                    self.rect.x = self.x
                if lr == 1:  # 向右前进
                    self.x += self.setting.alien_speed_factor
                    self.rect.x = self.x
            if ud:
                if ud == 'up':
                    self.y -= 10 * self.setting.alien_speed_factor
                    self.rect.y = self.y
                if ud == 'down':
                    self.y += 10 * self.setting.alien_speed_factor
                    self.rect.y = self.y

        edge()  # 重新更新碰壁信号
        if not self.edge:
            directory(lr=self.move_signal)
        else:
            directory(ud='down')
            self.move_signal *= -1
            directory(lr=self.move_signal)

    def blitem(self):
        """绘制敌机"""
        self.screen.blit(self.image, self.rect)
