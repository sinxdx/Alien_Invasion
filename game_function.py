import sys
from time import sleep

import pygame

import key_event
from alien import Alien


def check_events(screen, stats, setting, ship, bullets, button, bullets_debug):
    """检查事件，然后对事件进行分类，并分发到对应的函数中去"""

    def check_mouse_event(stats_in_mouse, play_button, mouse_x, mouse_y):
        """当玩家单击play_button时，游戏开始"""
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            stats_in_mouse.game_active = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_event.key_down(event, setting, screen, ship, bullets, bullets_debug, stats)
        elif event.type == pygame.KEYUP:
            key_event.key_up(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse_event(stats, button, mouse_x, mouse_y)


def object_update(ship, setting, screen, bullets, bullets_debug, aliens, stats):
    """用于对游戏中的几个对象：自机，子弹，敌机进行更新"""
    '''更新自机'''
    ship.update()
    if bullets_debug:
        bullets_debug.update(bullets)
    if bullets:
        bullets.update(bullets)
    if aliens:
        aliens.update()
    else:
        setting.increase_speed()
        creat_fleet(setting, screen, setting.alien_line, aliens)
    '''检测子弹是否与敌机发生碰撞'''
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collision = pygame.sprite.groupcollide(bullets_debug, aliens, True, True)
    '''检查自机是否与敌机发生碰撞'''
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(setting, stats, screen, ship, bullets, aliens)


def screen_update(screen, stats, auto_setting,
                  ship, bullets, aliens, button,
                  bullets_debug):
    """更新背景、自机、子弹，敌机然后绘制"""
    screen.fill(auto_setting.background_colour)  # 画出背景图图层
    ship.blitem()  # 在屏幕上画出自机
    """在这里可以这么理解，所谓面向对象，就是对于单独的某个对象，它自己能把所有的事情都做了。
    所以，在这里，screen这个对象能自己把自己画出来，而ship这个对象也要自己把自己更新并画出来"""
    '''绘制子弹'''
    if bullets:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
    '''绘制敌机'''
    if aliens:
        for alien in aliens.sprites():
            alien.blitem()
    '''游戏非活动时，绘制按钮'''
    if not stats.game_active:
        button.draw_button()
    if bullets_debug:
        for bullet_debug in bullets_debug.sprites():
            bullet_debug.draw_bullet()
    '''显示出绘制的屏幕'''
    pygame.display.flip()


def creat_fleet(setting, screen, line_num, aliens):
    """生成敌机舰队的函数
    读入：游戏设置，游戏主屏幕，给每个外星人分配的空间，要生成舰队的行数，以及要将生成舰队保存在aliens数组
    生成舰队的列数将由游戏屏幕宽度决定，一直生成到填满屏幕为止"""
    alien = Alien(setting, screen)
    reserve_space = setting.alien_reserve_space
    alien_sqrx = alien.rect.x + 2 * reserve_space  # 每个敌机需要占据的全部横向长度
    alien_sqry = alien.rect.y + 2 * reserve_space  # 每个敌机需要占据的全部纵向长度
    '''要计算生成一行生成几个敌机，需要用屏幕宽度去除以每个敌机占据的横向长度'''
    fleet_line = int(setting.screen_width / alien_sqrx - 1)
    for line in range(line_num):
        for column in range(fleet_line):
            alien = Alien(setting, screen)
            alien.x = reserve_space * (2 * column + 1)
            alien.y = reserve_space * (2 * line + 1)
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien)


def ship_hit(setting, stats, screen, ship, bullets, aliens):
    """当自机被撞到时
    自机生命值 -1, 自己恢复到原始位置
    清空子弹
    敌机消失，重置到原始状态
    暂停0.5秒"""
    '''自机生命值-1'''
    stats.ship_left -= 1
    ship.center_ship()
    '''清空子弹'''
    bullets.empty()
    '''重置敌机'''
    aliens.empty()
    creat_fleet(setting=setting, screen=screen, line_num=3, aliens=aliens)

    if stats.ship_left > 0:
        '''暂停游戏'''
        sleep(0.5)
    else:
        stats.game_active = False
