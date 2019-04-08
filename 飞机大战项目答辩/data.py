"""
定义数据模块
"""
import pygame

# 创建屏幕窗口
screen_rect = pygame.Rect(0, 0, 512, 750)
screen = pygame.display.set_mode((screen_rect.width, screen_rect.height), 0, 32)

# 英雄飞机图片
hero_images = [
    pygame.image.load("images/hero/hero.png")
]

# 背景图片
bg_images = [
    pygame.image.load("images/bg/step1.jpg"),
    pygame.image.load("images/bg/step2.jpg"),
    pygame.image.load("images/bg/step3.jpg")
]

# 开始界面图片
start_interface_images = [
    pygame.image.load("images/bg/screen.jpg"),
    pygame.image.load("images/bg/start.png"),
    pygame.image.load("images/bg/title.png")
]

# 英雄子弹图片
hero_bullet_images = [
    pygame.image.load("images/bullet/bullet1.png"),
    pygame.image.load("images/bullet/bullet2.png")
]

# 敌人飞机图片
enemy_images = [
    pygame.image.load("images/enemy/Enemy3.png"),
    pygame.image.load("images/enemy/Enemy4.png"),
    pygame.image.load("images/enemy/img_plane_enemy.png")
]
# 敌人子弹图片
enemy_bullet_images = [
    pygame.image.load("images/bullet/bullet.png")
]

