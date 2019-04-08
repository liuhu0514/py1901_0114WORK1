"""
飞机大战 V1.0
"""
import random
import pygame


class Resource:
    """系统初始资源数据"""
    # 游戏屏幕
    SCREEN_RECT = pygame.Rect(0, 0, 512, 768)
    # 敌人飞机创建事件
    ENEMY_EVENT_CREATE = pygame.USEREVENT
    # 资源精灵组
    GROUP_RESOURCE = pygame.sprite.Group()
    # 英雄精灵组
    GROUP_HERO = pygame.sprite.Group()
    # 敌机精灵组
    GROUP_ENEMY = pygame.sprite.Group()

    # 系统不同关卡背景图片
    STEP_BACKGROUND_IMAGE = ["./images/bg/step1.jpg",
                             "./images/bg/step2.jpg",
                             "./images/bg/step3.jpg",
                             "./images/bg/step4.jpg",
                             "./images/bg/step5.jpg",
                             "./images/bg/step6.jpg", ]
    # 系统不同关卡英雄飞机图片
    STEP_HERO_IMAEG = ["./images/hero/hero.png",
                       "./images/hero/hero.png",
                       "./images/hero/hero.png",
                       "./images/hero/hero.png",
                       "./images/hero/hero.png",
                       "./images/hero/hero.png", ]
    # 系统不同关卡地方飞机图片
    STEP_ENEMY_PLANE_SMALL = ["./images/enemy/Enemy3.png",
                              "./images/enemy/Enemy4.png",
                              "./images/enemy/Enemy3.png",
                              "./images/enemy/Enemy4.png",
                              "./images/enemy/Enemy3.png",
                              "./images/enemy/Enemy4.png",
                              ]
    # 敌人飞机爆炸图片
    ENEMY_PLANE_BOMP = [
        "./images/bomp/enemy3_down1.png",
        "./images/bomp/enemy3_down2.png",
        "./images/bomp/enemy3_down3.png",
        "./images/bomp/enemy3_down4.png",
        "./images/bomp/enemy3_down5.png",
        "./images/bomp/enemy3_down6.png",
        "./images/bomp/enemy3_down7.png",
        "./images/bomp/enemy3_down8.png",
    ]
    # 系统不同关卡背景速度
    STEP_BACKGROUND_SPEED = 1
    # 系统不同关卡飞机速度
    STEP_HERO_SPEED = 10
    # 系统不同关卡敌机速度
    STEP_ENEMY_PLANE_SMALL_SPEED = 3


class GameSprite(pygame.sprite.Sprite):
    """自定义游戏精灵对象"""

    def __init__(self, image_path, speed=1, x=0, y=0):
        super().__init__()
        # 初始化数据
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        """更新"""
        self.event()
        self.move()

    def event(self):
        """事件操作"""
        # 游戏退出事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                if event.type == pygame.QUIT:
                    # 用户点击了关闭按钮，游戏退出
                    pygame.quit()
                    exit()
                # 创建地方飞机的事件
                if event.type == Resource.ENEMY_EVENT_CREATE:
                    # 创建敌方飞机
                    enemy = EnemySprite("./images/enemy/enemy3.png", random.randint(3, 6))
                    # 添加敌方飞机精灵组
                    Resource.GROUP_ENEMY.add(enemy)

    def move(self):
        """移动及边界判断"""
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    """游戏背景精灵"""

    def move(self):
        """运动及边界判断"""
        super().move()
        # 边界判断
        if self.rect.y > Resource.SCREEN_RECT.height:
            self.rect.y = -Resource.SCREEN_RECT.height


class HeroSprite(GameSprite):

    def __init__(self, image_path, speed, x, y, bullet_image):
        super(HeroSprite, self).__init__(image_path, speed, x, y)
        # 子弹精灵组
        self.group_hero_bullet = pygame.sprite.Group()
        # 当前子弹图片
        self.bullet_image = bullet_image

    """英雄飞机"""

    def update(self):
        """更新：英雄飞机出厂后不需要运动，这里不需要调用父类的update()方法"""
        self.event()
        self.move()

    def event(self):
        """
        事件控制
        """
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            self.rect.x -= self.speed
            print("飞机向左移动")
        if key_down[pygame.K_RIGHT]:
            self.rect.x += self.speed
            print("飞机向右移动")
        if key_down[pygame.K_UP]:
            self.rect.y -= self.speed
            print("飞机向上移动")
        if key_down[pygame.K_DOWN]:
            self.rect.y += self.speed
            print("飞机向下移动")
        if key_down[pygame.K_SPACE]:
            self.fire()
            print("飞机发射子弹")

    def move(self):
        """边界判断"""
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > Resource.SCREEN_RECT.width - self.rect.width:
            self.rect.x = Resource.SCREEN_RECT.width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > Resource.SCREEN_RECT.height - self.rect.height:
            self.rect.y = Resource.SCREEN_RECT.height - self.rect.height

    def fire(self):
        """开火"""
        if len(self.group_hero_bullet) < 10:
            # 创建子弹：模拟~子弹上膛
            bullet = BulletSprite(self.bullet_image, 6, self.rect.x + 50, self.rect.y - 20)
            # 子弹添加到精灵组
            self.group_hero_bullet.add(bullet)


class BulletSprite(GameSprite):
    """子弹精灵类型"""

    def move(self):
        """移动及边界判断"""
        self.rect.y -= self.speed
        # 边界：
        if self.rect.y < 0:
            # 删除子弹
            self.kill()


class EnemySprite(GameSprite):
    """敌方飞机精灵类型"""

    def __init__(self, image_path, speed):
        super(EnemySprite, self).__init__(image_path, speed)
        # 随机横坐标 和 纵坐标
        self.rect.x = random.randint(0, Resource.SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

    def move(self):
        """地方飞机移动及边界判断"""
        self.rect.y += self.speed
        # 边界
        if self.rect.y > Resource.SCREEN_RECT.height:
            # 移除自己
            self.kill()

    def bomp(self, screen):
        """爆炸效果"""
        for img in Resource.ENEMY_PLANE_BOMP:
            screen.blit(pygame.image.load(img), self.rect)
            pygame.display.update()


class Engine:

    def __init__(self):
        """初始化资源数据"""
        # 游戏屏幕
        self.screen = pygame.display.set_mode((Resource.SCREEN_RECT.width, Resource.SCREEN_RECT.height), 0, 32)
        # 游戏积分
        self.score = 0
        # 游戏关卡
        self.step = 1
        # 创建敌机定时器
        pygame.time.set_timer(Resource.ENEMY_EVENT_CREATE, 1000)
        # 关卡分数设置
        self.step_score_list = [10, 20, 30, 40, 50]

    def run(self):
        """开始游戏"""
        Resource.GROUP_RESOURCE.empty()
        Resource.GROUP_HERO.empty()
        Resource.GROUP_ENEMY.empty()
        # 加载背景资源
        background1 = BackgroundSprite(Resource.STEP_BACKGROUND_IMAGE[self.step-1])
        background2 = BackgroundSprite(Resource.STEP_BACKGROUND_IMAGE[self.step-1])
        background2.rect.y = -background2.rect.height

        Resource.GROUP_RESOURCE.add(background1, background2)

        # 加载英雄飞机资源
        hero = HeroSprite(Resource.STEP_HERO_IMAEG[self.step-1], Resource.STEP_HERO_SPEED,
                          Resource.SCREEN_RECT.centerx, Resource.SCREEN_RECT.centery + 200,
                          "./images/bullet/bullet3.png")
        Resource.GROUP_HERO.add(hero)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.__event()
            self.__update()
            self.__collide()

            if self.score in self.step_score_list:
                self.score += 1
                self.step += 1
                self.__grow()
                return self.run()

    def __grow(self):
        """关卡升级过度动画：持续2S钟"""
        pass

    def __update(self):
        """更新场景"""
        Resource.GROUP_RESOURCE.update()
        Resource.GROUP_RESOURCE.draw(self.screen)

        Resource.GROUP_HERO.update()
        Resource.GROUP_HERO.draw(self.screen)

        Resource.GROUP_ENEMY.update()
        Resource.GROUP_ENEMY.draw(self.screen)

        # 更新英雄飞机子弹
        for hero in Resource.GROUP_HERO:
            hero.group_hero_bullet.update()
            hero.group_hero_bullet.draw(self.screen)

        pygame.display.update()

    def __event(self):
        """事件控制"""
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 游戏结束事件控制
                if event.type == pygame.QUIT:
                    pygame.quit()

                # 地方飞机创建
                if event.type == Resource.ENEMY_EVENT_CREATE:
                    # 创建敌人小飞机
                    enemy = EnemySprite(Resource.STEP_ENEMY_PLANE_SMALL[self.step - 1],
                                        Resource.STEP_ENEMY_PLANE_SMALL_SPEED * self.step)
                    # 添加精灵组
                    Resource.GROUP_ENEMY.add(enemy)

    def __collide(self):
        """碰撞检测"""
        # 英雄飞机子弹  vs  敌人飞机
        for hero in Resource.GROUP_HERO:
            res = pygame.sprite.groupcollide(hero.group_hero_bullet, Resource.GROUP_ENEMY, True, True)
            # 增加积分
            if len(res.keys()) > 0:
                self.score += 1
                print("=========>", self.score)
            if len(res.values()) > 0:
                for enemy in res.values():
                    enemy[0].bomp(self.screen)

        # 英雄飞机 vs  敌人飞机
        res = pygame.sprite.groupcollide(Resource.GROUP_HERO, Resource.GROUP_ENEMY, True, True)
        if len(res.keys()) > 0:
            print("英雄死亡，游戏退出...")
            pygame.quit()


Engine().run()
