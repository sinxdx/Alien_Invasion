import sys

import pygame

import key_event
from alien import Alien


def check_events(check_events_screen, check_events_setting, check_events_ship, check_events_bullets):
    """检查事件，然后对键盘事件进行分类，并分发到对应的函数中去"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_event.key_down(event, check_events_setting, check_events_screen, check_events_ship,
                               check_events_bullets)
        elif event.type == pygame.KEYUP:
            key_event.key_up(event, check_events_ship, )


def object_update(ship, bullets, aliens):
    """用于对游戏中的几个对象：自机，子弹，敌机进行更新"""
    '''更新自机'''
    ship.update()
    if bullets:
        bullets.update(bullets)
    if aliens:
        aliens.update()
    '''检测子弹是否与敌机发生碰撞'''
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    '''检查自机是否与敌机发生碰撞'''
    if pygame.sprite.spritecollideany(ship, aliens):
        print("游戏结束")


def screen_update(screen, auto_setting, ship, bullets, aliens):
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
    else:
        creat_fleet(auto_setting, screen, 3, aliens)
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
    每行生成的外星人数量 = int(setting.screen_width / alien_sqrx - 1)
    for line in range(line_num):
        for column in range(每行生成的外星人数量):
            alien = Alien(setting, screen)
            alien.x = reserve_space * (2 * column + 1)
            alien.y = reserve_space * (2 * line + 1)
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien)
