"""
V2.0 游戏资源加载
"""
import pygame

# 初始化创建
pygame.init()
# 创建游戏区域对象
screen = pygame.display.set_mode((512, 768), 0, 32)

#############################
# 背景
background = pygame.image.load("../images/bg/step1.jpg")
# 填充背景
screen.blit(background, (0, 0))

# 英雄飞机
hero = pygame.image.load("../images/hero/hero.png")
# 填充英雄飞机
screen.blit(hero, (196, 650))
##############################

# 场景循环
while True:
    # 渲染展示
    pygame.display.update()

# 退出
pygame.quit()
