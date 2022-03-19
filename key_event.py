import pygame as pg
from bullet import Bullet


def key_down(event, key_down_setting, key_down_screen, key_down_ship, key_down_bullets):
    """用于按键按下之后的操作"""
    if event.key == pg.K_LEFT:
        key_down_ship.moving_left = True
    elif event.key == pg.K_RIGHT:
        key_down_ship.moving_right = True
    elif event.key == pg.K_UP:
        key_down_ship.moving_up = True
    elif event.key == pg.K_DOWN:
        key_down_ship.moving_down = True
    '''在每次按下z键时，都往bullets组里添加一颗子弹'''
    if event.key == pg.K_z:  # 当按下z键时发射子弹
        '''创建子弹，然后加到bullets这个Group中去'''
        fire_bullet(key_down_setting, key_down_screen, key_down_ship, key_down_bullets)


def key_up(event, ship):
    """用于抬起按键之后的操作"""
    if event.key == pg.K_LEFT:
        ship.moving_left = False
    elif event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_UP:
        ship.moving_up = False
    elif event.key == pg.K_DOWN:
        ship.moving_down = False


def fire_bullet(setting, screen, ship, bullets):
    new_bullet = Bullet(setting, screen, ship, bullets)
    bullets.add(new_bullet)
