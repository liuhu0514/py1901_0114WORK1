"""
v1.0
    场景搭建
    注意：推荐在Unix/Linux中开发
"""
import pygame

# 初始化
pygame.init()
# 创建游戏区域
screen = pygame.display.set_mode((512, 768), 0, 32)

#####################################################

# 背景
background = pygame.image.load("./images/bg/step5.jpg")
# # 背景填充
# screen.blit(background, (0, 0))

# 英雄飞机
hero = pygame.image.load("./images/hero/hero.png")
# 填充英雄飞机
# screen.blit(hero, (196, 650))
hero_position_x = 196
hero_position_y = 650

#####################################################


# 场景循环
while True:
    #######################################################
    # 事件：用户执行的操作随时可能发生，所以代码要添加到循环中
    # event_list = pygame.event.get()

    # 渲染场景
    pygame.display.update()

# 游戏退出
pygame.quit()
