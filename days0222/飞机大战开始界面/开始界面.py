"""
飞机大战界面初开发
"""

import pygame
import random, sys, os, math

# 初始化
pygame.init()

# 添加音乐
pygame.mixer.music.load("plane/sound/game_music.mp3")
pygame.mixer.music.play()

# 创建一个时钟
clock = pygame.time.Clock()


# 游戏控制开关
is_play = False

# 设置窗口大小
screen_rect = pygame.Rect(0, 0, 480, 700)
screen = pygame.display.set_mode((screen_rect.width, screen_rect.height))

# 开始界面的图片
start_images = [
    pygame.image.load("plane/image/background.png"),
    pygame.image.load("plane/image/name.png"),
    pygame.transform.scale(pygame.image.load("plane/image/loading.png"), (screen_rect.width, screen_rect.width)),
    pygame.image.load("plane/image/icon72x72.png")
]

# 开始界面下方的三张图
start_three_images = [
    pygame.image.load("plane/image/game_loading1.png"),
    pygame.image.load("plane/image/game_loading2.png"),
    pygame.image.load("plane/image/game_loading3.png")
]

# 英雄飞机图片
hero_images = [
    pygame.image.load("plane/image/hero2.png"),
    pygame.image.load("plane/image/hero1.png")
]

# 子弹图片列表
bullet_images = [
    pygame.image.load("plane/image/bullet2.png")
]

# 子弹存储列表
bullets = []


class StartPanel:
    """开始界面类"""

    is_in = False

    def __init__(self, images, three_images, screen):
        # 开始界面用到的图片
        self.images = images
        # 开始界面底部用到的界面
        self.three_images = three_images
        # 游戏窗口
        self.screen = screen
        # 累加变量控制三张图的速度
        self.add_three = 0
        # 底部三张动图的索引
        self.three_index = 0
        # sin变量
        self.sinY = 0

    def display(self):

        # 背景
        self.screen.blit(self.images[0], (0, 0))
        # 开始标题
        self.sinY += 0.1
        if self.sinY == 3:
            self.sinY = 0
        self.screen.blit(self.images[1], ((screen_rect.width-self.images[1].get_rect().width)/2,
                                          100+50*math.sin(self.sinY)))
        # 圆环效果
        self.screen.blit(self.images[2], (0, (screen_rect.height-self.images[2].get_rect().height)/2))
        # 按钮
        button_rect = self.screen.blit(self.images[3], ((screen_rect.width-self.images[3].get_rect().width)/2,
                                        (screen_rect.height-self.images[3].get_rect().height)/2))
        StartPanel.is_in = button_rect.collidepoint(pygame.mouse.get_pos())
        # 底部三张图
        self.screen.blit(self.three_images[self.three_index],
                         ((screen_rect.width-self.three_images[2].get_rect().width)/2, 600))
        self.add_three += 1
        # 判断三张图片的出现的频率
        if self.add_three == 20:
            self.three_index += 1
            if self.three_index == 3:
                self.three_index = 0
            self.add_three = 0


class GameBg:
    """游戏背景类"""
    def __init__(self, image, screen, speed):
        # 背景图片1
        self.image1 = image
        # 背景图片2
        self.image2 = image.copy()
        # 背景图片区域1
        self.rect1 = self.image1.get_rect()
        # 背景区域2
        self.rect2 = self.image2.get_rect()
        self.rect2.y = -self.rect2.height
        # 屏幕
        self.screen = screen
        # 移动速度
        self.speed = speed

    def display(self):
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)
        # 移动
        self.rect1 = self.rect1.move(0, self.speed)
        self.rect2 = self.rect2.move(0, self.speed)
        if self.rect1.y > self.rect1.height:
            self.rect1.y = -self.rect1.height
        if self.rect2.y > self.rect2.height:
            self.rect2.y = -self.rect2.height


class Hero:
    """英雄飞机类"""

    is_down = False

    def __init__(self, images, screen, pos, speed, hp):
        self.images = images
        self.image1 = self.images[0]
        self.image2 = self.images[1]
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect1.center = pos
        self.screen = screen
        self.speed = speed
        self.hp = hp
        # 索引
        self.index = 0
        # 刷新次数累加
        self.add_index = 0
        # 射击累加变量
        self.add_shoot = 0

    def display(self):
        """渲染飞机"""

        self.move()

        # 喷漆图片切换
        self.add_index += 1
        if self.add_index == 10:
            self.index += 1
            if self.index == 2:
                self.index = 0
            self.add_index = 0
        self.ctrl()
        self.shoot()
        # 渲染显示英雄飞机
        self.screen.blit(self.images[self.index], self.rect1)

    def ctrl(self):
        """英雄控制"""
        # 鼠标控制
        tmp1 = self.rect1.collidepoint(pygame.mouse.get_pos())
        tmp2 = self.rect2.collidepoint(pygame.mouse.get_pos())
        if (tmp1 or tmp2) and Hero.is_down:
            self.rect1.center = pygame.mouse.get_pos()
            self.rect2.center = pygame.mouse.get_pos()
        # 键盘控制
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_UP]:
            self.rect1.y -= self.speed

        elif key_down[pygame.K_DOWN]:
            self.rect1.y += self.speed

        elif key_down[pygame.K_LEFT]:
            self.rect1.x -= self.speed

        elif key_down[pygame.K_RIGHT]:
            self.rect1.x += self.speed

    def move(self):
        """边界判断"""
        if self.rect1.x < 0:
            self.rect1.x = 0
        elif self.rect2.x < 0:
            self.rect2.x = 0

        elif self.rect1.x > screen_rect.width - self.rect1.width:
            self.rect1.x = screen_rect.width - self.rect1.width
        elif self.rect2.x > screen_rect.width - self.rect2.width:
            self.rect2.x = screen_rect.width - self.rect2.width

        elif self.rect1.y < 0:
            self.rect1.y = 0
        elif self.rect2.y < 0:
            self.rect2.y = 0

        elif self.rect1.y > screen_rect.height - self.rect1.height:
            self.rect1.y = screen_rect.height - self.rect1.height
        elif self.rect2.y > screen_rect.height - self.rect2.height:
            self.rect2.y = screen_rect.height - self.rect2.height

    def shoot(self):
        """射击"""
        self.add_shoot += 1
        if self.add_shoot == 10:
            Bullet(bullet_images[0], self.screen, hero.rect1.midtop, 5)
            self.add_shoot = 0
        for i in bullets:
            i.display()
        print(len(bullets))


class Bullet:
    """子弹类"""
    def __init__(self, image, screen, pos, speed):
        """
        初始化属性
        :param image: 子弹图片
        :param screen: 屏幕
        :param pos: 初始位置
        :param speed: 移动速度
        """
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.screen = screen
        self.speed = speed
        # 将产生的子弹添加到列表中
        bullets.append(self)

    def display(self):
        """渲染"""
        self.screen.blit(self.image, self.rect)
        self.move()

    def move(self):
        """移动"""
        self.rect = self.rect.move(0, -self.speed)
        # 出屏幕判断死亡
        if self.rect.y < -self.rect.height:
            bullets.remove(self)


# 开始界对象
start_panel = StartPanel(start_images, start_three_images, screen)

# 游戏背景对象
game_bg = GameBg(start_images[0], screen, 2)

# 英雄飞机对象
hero = Hero(hero_images, screen, (screen.get_rect().centerx, 600), 5, 3)


def all_event():
    """所有检测事件"""
    global is_play
    for event in pygame.event.get():
        # 判断关闭游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 鼠标控制事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Hero.is_down = True
                if StartPanel.is_in == 1:
                    is_play = True

        if event.type == pygame.MOUSEBUTTONUP:
                Hero.is_down = False

        # 键盘事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_play = False


def main():
    while True:
        # 控制画面频率
        clock.tick(60)
        # 监控所有事件
        all_event()

        # 判断是否开始游戏
        if is_play:
            # 游戏开始
            game_bg.display()
            hero.display()

        else:
            # 开始界面
            start_panel.display()

        # 刷新屏幕
        pygame.display.update()


if __name__ == "__main__":
    main()
