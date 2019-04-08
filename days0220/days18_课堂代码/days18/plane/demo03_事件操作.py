"""
V3.0 游戏资源事件操作
"""
import pygame, sys

# 初始化创建
pygame.init()
# 创建游戏区域对象
screen = pygame.display.set_mode((512, 768), 0, 32)

# 背景
background = pygame.image.load("../images/bg/step1.jpg")

# 英雄飞机
hero = pygame.image.load("../images/hero/hero.png")
hero_position_x = 196
hero_position_y = 650

# 场景循环
while True:
    #################################################
    # 事件：用户执行的操作随时可能发生，所以代码要添加到循环中
    event_list = pygame.event.get()
    # 判断如果发生事件行为
    if len(event_list) > 0:
        print(event_list)
        # 循环获取事件
        for event in event_list:
            # 判断是否退出事件
            if event.type == pygame.QUIT:
                # 游戏结束
                # 退出
                pygame.quit()
                sys.exit(1)

            # 键盘上按键被按下
            if event.type == pygame.KEYDOWN:
                # 上
                if event.key == pygame.K_UP:
                    print("飞机向上移动^^^^^^^^^^^^")
                    hero_position_y -= 5
                # 下
                elif event.key == pygame.K_DOWN:
                    print("飞机向下移动vvvvvvvvvvvv")
                    hero_position_y += 5
                # 左
                elif event.key == pygame.K_LEFT:
                    print("飞机向左移动<<<<<<<<<<<<")
                    hero_position_x -= 5
                # 右
                elif event.key == pygame.K_RIGHT:
                    print("飞机向右移动>>>>>>>>>>>>")
                    hero_position_x += 5
                elif event.key == pygame.K_SPACE:
                    print("飞机开火===============")
    #################################################
    # 填充背景
    screen.blit(background, (0, 0))
    # 飞机动画
    # hero_position_y -= 1
    # 边界判断
    if hero_position_y < -80:
        hero_position_y = 768
    # 填充英雄飞机
    screen.blit(hero, (hero_position_x, hero_position_y))
    #################################################

    # 渲染展示
    pygame.display.update()


