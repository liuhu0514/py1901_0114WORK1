"""
函数模块
"""

import models, data
import pygame

pygame.init()
clock = pygame.time.Clock()
# 控制游戏是否开始
is_play = False


# 创建开始界面
# 开始界面背景
start_interface = models.StartSprite(data.start_interface_images, 0)

# 游戏背景
game_bg = models.BgSprite(data.bg_images[0], 2)

# 英雄飞机
hero = models.HeroSprite(data.hero_images[0], (data.screen_rect.centerx, 700), 5, 3)


def all_event():
    global is_play
    event_list = pygame.event.get()
    if len(event_list) > 0:
        for event in event_list:
            # 退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and models.StartSprite.is_in == 1:
                    is_play = True


def start():
    # 开始界面
    while True:
        # 事件监听
        all_event()
        clock.tick(60)

        if is_play:
            game_bg.display()
            hero.display()

        else:
            start_interface.display()

        # 更新场景
        pygame.display.update()


start()
