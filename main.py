# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Union

import pygame
from pygame.surface import Surface, SurfaceType
from pygame.sprite import Group
from ship import Ship
from Setting import Settings
import game_function as gf
from game_status import GameStats
from button import Button


def run_game():
    """游戏初始化"""
    pygame.init()
    auto_setting = Settings()
    screen: Union[Surface, SurfaceType] = pygame.display.set_mode(
        (auto_setting.screen_width, auto_setting.screen_height))
    pygame.display.set_caption('东方千夜阁')

    '''创建自机'''
    ship = Ship(auto_setting, screen)
    '''创建子弹编组'''
    bullets = Group()  # 创建一个空组用来存放子弹，但目前还不往里面放子弹，要到发射子弹时，才往里面存子弹
    bullets_debug = Group()
    '''创建敌机舰队'''
    aliens = Group()
    gf.creat_fleet(auto_setting, screen, auto_setting.alien_line, aliens)
    '''创建游戏统计数据'''
    stats = GameStats(auto_setting)
    '''创建开始按钮'''
    button: Button = Button(screen=screen, msg="Play")
    '''游戏的主循环'''
    while True:
        '''监视鼠标和键盘事件'''
        gf.check_events(screen=screen, stats=stats, setting=auto_setting,
                        ship=ship, bullets=bullets, button=button,
                        bullets_debug=bullets_debug)
        '''更新物品，包括子弹和飞船'''
        if stats.game_active:
            # 自机生命值大于0， 则游戏继续
            gf.object_update(setting=auto_setting, screen=screen, stats=stats,
                             ship=ship, bullets=bullets, aliens=aliens,
                             bullets_debug=bullets_debug)
        '''绘制屏幕，绘制自机，绘制子弹，然后显示'''
        gf.screen_update(screen, stats, auto_setting,
                         ship, bullets, aliens, button,
                         bullets_debug)


'''运行游戏'''
run_game()
