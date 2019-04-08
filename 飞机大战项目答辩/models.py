"""
类型模块
"""
import pygame
import sys
import data

screen = data.screen
screen_rect = data.screen_rect


class StartSprite:
    """自定义游戏精灵"""

    # 鼠标是否在按钮里
    is_in = False

    def __init__(self, images, speed=2):
        super().__init__()
        self.images = images
        # 移动速度
        self.speed = speed

    def display(self):
        """开始界面显示"""
        # 开始背景
        data.screen.blit(self.images[0], (0, 0))
        # 游戏标题
        data.screen.blit(self.images[2], (110, 100))
        # 游戏按钮
        x = data.screen.blit(self.images[1], (data.screen_rect.centerx, data.screen_rect.centery))
        StartSprite.is_in = x.collidepoint(pygame.mouse.get_pos())

    def update(self):
        """更新"""
        # 默认运动
        self.event()


class BgSprite(pygame.sprite.Sprite):
    """背景精灵"""
    def __init__(self, image, speed):
        super().__init__()
        self.image = image
        self.image1 = image.copy()
        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()
        self.rect1.y = -self.rect1.height
        self.speed = speed

    def display(self):
        """显示渲染"""
        data.screen.blit(self.image, self.rect)
        data.screen.blit(self.image1, self.rect1)
        # 屏幕移动
        self.move()

    def move(self):
        """移动"""
        self.rect.y += self.speed
        self.rect1.y += self.speed
        if self.rect.y > self.rect.height:
            self.rect.y = -self.rect.height
        if self.rect1.y > self.rect1.height:
            self.rect1.y = -self.rect1.height


class HeroSprite(pygame.sprite.Sprite):
    """英雄飞机精灵"""
    def __init__(self, image, pos, speed, hp):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed
        self.score = 0
        self.hp = hp

    def display(self):
        """显示渲染"""
        self.move()
        self.ctrl()
        screen.blit(self.image, self.rect)
        self.move()

    def ctrl(self):
        """控制"""
        # 键盘控制
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_UP]:
            self.rect.y -= self.speed

        if key_down[pygame.K_DOWN]:
            self.rect.y += self.speed

        if key_down[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key_down[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def move(self):
        """移动边界判断"""
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x >= screen_rect.width - self.rect.width:
            self.rect.x = screen_rect.width - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.y >= screen_rect.height - self.rect.height:
            self.rect.y = screen_rect.height - self.rect.height


class BulletSprite(pygame.sprite.Sprite):
    """子弹精灵组"""
    def __init__(self, images, ):
        pass
