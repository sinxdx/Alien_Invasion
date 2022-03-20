import pygame as pg
from bullet import Bullet
from bullet_debug import BulletDebug


def key_down(event, key_down_setting, key_down_screen, key_down_ship, key_down_bullets, bullets_debug, stats):
    """用于按键按下之后的操作"""
    if event.key == pg.K_LEFT:
        key_down_ship.moving_left = True
    elif event.key == pg.K_RIGHT:
        key_down_ship.moving_right = True
    elif event.key == pg.K_UP:
        key_down_ship.moving_up = True
    elif event.key == pg.K_DOWN:
        key_down_ship.moving_down = True
    elif event.key == pg.K_p:
        stats.game_active = not stats.game_active
    if event.key == pg.K_z:  # 当按下z键时发射子弹
        '''创建子弹，然后加到bullets这个Group中去'''
        fire_bullet(key_down_setting, key_down_screen, key_down_ship, key_down_bullets)
    if event.key == pg.K_f:  # 当按下f键时发射大子弹（调试用）
        fire_bullet_debug(key_down_setting, key_down_screen, key_down_ship, bullets_debug)


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
    new_bullet = Bullet(setting, screen, ship)
    bullets.add(new_bullet)


def fire_bullet_debug(setting, screen, ship, bullets_debug):
    new_bullet = BulletDebug(setting, screen, ship)
    bullets_debug.add(new_bullet)
