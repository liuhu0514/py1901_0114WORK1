import pygame
import random
import os
pygame.font.init()


class Resource:
    """系统初始化资源"""

    # 游戏屏幕
    screen_rect = pygame.Rect(0, 0, 512, 768)
    # 敌人飞机创造事件
    enemy_event_create = pygame.USEREVENT
    # 资源精灵组
    group_resource = pygame.sprite.Group()
    # 英雄精灵组
    group_hero = pygame.sprite.Group()
    # 英雄子弹精灵组
    group_hero_bullet = pygame.sprite.Group()
    # 敌机精灵组
    group_enemy = pygame.sprite.Group()
    # 敌机子弹组
    group_enemy_bullet = pygame.sprite.Group()
    # 跳转精灵组
    group_jump = pygame.sprite.Group()

    # 英雄飞机图片
    hero_images = [
        "images/hero/hero.png"
    ]

    # 背景图片
    bg_images = [
        "images/bg/step1.jpg",
        "images/bg/step2.jpg",
        "images/bg/step3.jpg",
        "images/bg/step4.jpg",
        "images/bg/step5.jpg",
        "images/bg/step6.jpg"
    ]

    # 开始界面图片
    start_interface_images = [
        "images/bg/screen.jpg",
        "images/bg/start.png",
        "images/bg/title.png"
    ]

    # 英雄子弹图片
    hero_bullet_images = [
        "images/bullet/bullet1.png",
        "images/bullet/bullet2.png"
    ]

    # 敌人飞机图片
    enemy_images = [
        "images/enemy/Enemy3.png",
        "images/enemy/Enemy4.png",
        "images/enemy/img_plane_enemy.png"
    ]
    # 敌人子弹图片
    enemy_bullet_images = [
        "images/bullet/enemy_bullet1.png"
    ]
    # 关卡背景图
    jump_images = [
        "images/jump/num1.png",
        "images/jump/num2.png",
        "images/jump/num3.png",
        "images/jump/num4.png",
        "images/jump/num5.png",
        "images/jump/num6.png"
    ]
    # 系统不同关卡背景速度
    step_background_speed = 1
    # 不同关卡飞机速度
    step_hero_speed = 5
    # 系统不同关卡敌机速度
    step_enemy_speed = 3
    clock = pygame.time.Clock()
    # 判断游戏是否开始
    is_play = False
    # 游戏中字体
    font = pygame.font.Font("font/aaa.ttf", 30)
    # 死亡得分字体
    dead_font = pygame.font.Font("font/aaa.ttf", 50)
    # 死亡创造最高分字体
    dead_height_font = pygame.font.Font("font/aaa.ttf", 30)
    # 历史分数
    history_score = 0


class StartSprite:
    """开始界面"""

    # 鼠标是否在按钮里
    is_in = False

    def __init__(self, images, screen):
        super().__init__()
        self.images = images
        self.screen = screen

    def display(self):
        """开始界面显示"""
        self.event()
        # 开始背景
        self.screen.blit(pygame.image.load(self.images[0]), (0, 0))
        self.screen.blit(Resource.font.render(f"历史最高分数为{Resource.history_score}", True, (255, 0, 0)), (30, 520))
        # 游戏标题
        self.screen.blit(pygame.image.load(self.images[2]), (110, 100))
        # 游戏按钮
        x = self.screen.blit(pygame.image.load(self.images[1]), (Resource.screen_rect.centerx,
                                                                 Resource.screen_rect.centery))
        StartSprite.is_in = x.collidepoint(pygame.mouse.get_pos())

    def event(self):
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 游戏结束事件控制
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # 是否开始游戏控制
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and StartSprite.is_in == 1:
                        Resource.is_play = True


class GameSprite(pygame.sprite.Sprite):
    """自定义游戏精灵"""

    def __init__(self, screen, image, speed, x=0, y=0):
        super().__init__()
        # 初始化数据
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.screen = screen

    def update(self):
        """更新"""
        self.event()
        self.move()

    def event(self):
        """事件操作"""
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                if event.type == pygame.QUIT:
                    # 点击关闭，关闭游戏
                    pygame.quit()
                    exit()

    def move(self):
        """移动及边界判断"""
        self.rect.y += self.speed+engine.step


class BgSprite(GameSprite):
    """游戏背景精灵"""
    def move(self):
        """运动及边界判断"""
        super().move()
        # 判断边界
        if self.rect.y > self.rect.height:
            self.rect.y = -self.rect.height


class HeroSprite(GameSprite):
    """英雄飞机精灵"""
    def __init__(self, screen, image, speed, x, y, bullet_image):
        super().__init__(screen, image, speed, x, y)
        # 子弹精灵组
        # self.
        # 当前子弹图片
        self.bullet_image = bullet_image
        # 控制子弹发射频率
        self.bullet_rate = 0
        self.screen = screen
        self.hp = 3

    def update(self):
        """跟新：英雄飞机出厂后不需要运动，这里不需要调用父类的update()方法"""
        self.event()
        self.move()
        self.fire()

    def event(self):
        """事件控制"""
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if key_down[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if key_down[pygame.K_UP]:
            self.rect.y -= self.speed

        if key_down[pygame.K_DOWN]:
            self.rect.y += self.speed

    def move(self):
        """边界判断"""
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > Resource.screen_rect.width - self.rect.width:
            self.rect.x = Resource.screen_rect.width - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > Resource.screen_rect.height - self.rect.height:
            self.rect.y = Resource.screen_rect.height - self.rect.height

    def fire(self):
        """开火"""
        self.bullet_rate += 1
        if self.bullet_rate == 15-engine.step:
            bullet = BulletSprite(self.screen, self.bullet_image, 5, self.rect.x + 22, self.rect.y - 30)
            Resource.group_hero_bullet.add(bullet)
            self.bullet_rate = 0


class BulletSprite(GameSprite):
    """子弹精灵类型"""

    def move(self):
        """移动及边界判断"""
        self.rect.y -= self.speed
        # 边界判断
        if self.rect.y < 0:
            # 删除子弹
            self.kill()


class EnemyBulletSprite(GameSprite):
    """子弹精灵类型"""

    def move(self):
        """移动及边界判断"""
        self.rect.y += self.speed
        # 边界判断
        if self.rect.y > Resource.screen_rect.height:
            # 删除子弹
            self.kill()


class EnemySprite(GameSprite):
    """敌方精灵类型"""

    def __init__(self, screen, image, speed, hp, integral):
        super().__init__(screen, image, speed)
        # 随机横坐标 和 纵坐标
        self.rect.x = random.randint(0, Resource.screen_rect.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = hp
        # 分值
        self.integral = integral
        self.screen = screen
        self.bullet_rate = 0

    def update(self):
        """更新"""
        super().update()
        self.event()
        self.move()
        self.fire()

    def move(self):
        """敌方飞机移动及边界判断"""
        self.rect.y += self.speed
        # 边界
        if self.rect.y > Resource.screen_rect.height:
            # 移除自己
            self.kill()

    def event(self):
        """事件监控"""
        if self.hp <= 0:
            self.kill()

    def fire(self):
        """开火"""
        self.bullet_rate += 1
        if self.bullet_rate == 50 - engine.step*2:
            bullet = EnemyBulletSprite(self.screen, Resource.enemy_bullet_images[0], self.speed+2,
                                       self.rect.x + self.rect.width/2, self.rect.y + self.rect.height)
            Resource.group_enemy_bullet.add(bullet)

            self.bullet_rate = 0


class JumpSprite(pygame.sprite.Sprite):
    """跳转界面"""

    def __init__(self, screen, image, speed, x, y):
        super().__init__()
        # 初始化数据
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.screen = screen

    def update(self):
        """更新"""
        self.event()
        self.move()

    def event(self):
        """事件操作"""
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                if event.type == pygame.QUIT:
                    # 点击关闭，关闭游戏
                    pygame.quit()
                    exit()

    def move(self):
        """移动及边界判断"""
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.rect.y = 0


class Dead:
    """死亡界面"""
    is_click = False

    def __init__(self, images, screen, score):
        self.images = images
        self.screen = screen
        self.score = score

    def display(self):
        """开始界面显示"""
        self.event()
        # 开始背景
        res = self.screen.blit(pygame.image.load(self.images), (0, 0))
        self.screen.blit(Resource.font.render(f"您死在了", True, (255, 255, 255)), (30, 320))

        self.screen.blit(Resource.dead_font.render(f"您的分数为{self.score}", True, (255, 0, 0)), (100, 400))

        Dead.is_click = res.collidepoint(pygame.mouse.get_pos())
        if self.score > Resource.history_score:
            self.screen.blit(Resource.dead_height_font.render(f"您当前创造可历史最高分：{self.score}", True, (255, 0, 0)), (80, 200))
        else:
            self.screen.blit(Resource.dead_font.render(f"历史最高分为：{Resource.history_score}", True, (255, 0, 0)), (80, 200))

    def event(self):
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 游戏结束事件控制
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # 是否开始游戏控制
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and Dead.is_click == 1:
                        Resource.is_play = False


class Engine:
    """引擎类"""
    def __init__(self):
        """初始化资源"""
        # 游戏屏幕
        self.screen = pygame.display.set_mode((Resource.screen_rect.width, Resource.screen_rect.height), 0, 32)
        # 游戏分数
        self.score = 0
        # 游戏关卡
        self.step = 1
        # 创建敌机定时器
        pygame.time.set_timer(Resource.enemy_event_create, random.randint(1000/self.step, 3000/self.step))
        # 关卡分数设置
        self.step_score_list = [500, 1000, 2500, 5000, 10000, 100000]
        self.hp = 3
        self.add_jump = 0

    def run(self):
        pygame.init()
        pygame.display.set_caption("雷霆战机！")
        pygame.display.set_icon(pygame.image.load("images/icon/icon.png"))
        pygame.mixer.music.load("sound/zhengfutiantang.ogg")
        pygame.mixer.music.play(-1)
        # 读取历史最高分
        self.read_history()
        """开始游戏"""

        # 清空精灵组
        Resource.group_resource.empty()
        Resource.group_hero.empty()
        Resource.group_enemy.empty()
        start = StartSprite(Resource.start_interface_images, self.screen)
        while True:
            if Resource.is_play:
                if self.step > 6:
                    Resource.is_play = False
                    self.step = 1
                    return self.run()
                jump = JumpSprite(self.screen, Resource.jump_images[self.step-1], 8, 0, Resource.screen_rect.height)
                Resource.group_jump.add(jump)
                pygame.mixer.music.stop()

                # 游戏开始循环
                while True:
                    pygame.mixer.music.load("sound/game_music.ogg")
                    pygame.mixer.music.play(-1)
                    # 游戏刷新频率控制
                    Resource.clock.tick(60)
                    self.add_jump += 1
                    self.update1()

                    if self.add_jump == 156:
                        self.add_jump = 0
                        Resource.group_jump.empty()
                        # 加载背景资源
                        bg1 = BgSprite(self.screen, Resource.bg_images[self.step - 1], 1)
                        bg2 = BgSprite(self.screen, Resource.bg_images[self.step - 1], 1)
                        bg2.rect.y = -bg2.rect.height

                        Resource.group_resource.add(bg1, bg2)

                        # 加载英雄
                        hero = HeroSprite(self.screen, Resource.hero_images[0], 5,
                                          Resource.screen_rect.centerx - 60,
                                          Resource.screen_rect.centery + 240,
                                          Resource.hero_bullet_images[1])

                        Resource.group_hero.add(hero)

                        while True:
                            Resource.clock.tick(60)
                            # 游戏开始
                            self.all_event()
                            self.update()
                            self.collide()

                            # 判断是否进入下一关
                            if self.score >= self.step_score_list[self.step-1]:
                                Resource.group_enemy_bullet.empty()
                                Resource.group_enemy.empty()
                                Resource.group_hero_bullet.empty()
                                self.score += 1
                                self.step += 1
                                return self.run()

            else:
                # 展示开始界面
                start.display()

            # 刷新屏幕
            pygame.display.update()

    def all_event(self):
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 游戏结束事件控制
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # 是否开始游戏控制
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and StartSprite.is_in == 1:
                        Resource.is_play = True

                # 敌方飞机创建
                if event.type == Resource.enemy_event_create:
                    enemy1 = EnemySprite(self.screen, Resource.enemy_images[0], random.randint(self.step+1, self.step+3),
                                         1, 12)
                    enemy2 = EnemySprite(self.screen, Resource.enemy_images[1], random.randint(self.step+1, self.step+2),
                                         3, 23)
                    enemy3 = EnemySprite(self.screen, Resource.enemy_images[2], random.randint(self.step, self.step+1),
                                         5, 33)
                    if self.step <= 3:
                        enemy_list = [enemy1, enemy2, enemy3, enemy1, enemy1, enemy2, enemy2]
                        enemys = random.sample(enemy_list, random.randint(self.step+1, self.step+3))
                        # # 添加到精灵组
                        Resource.group_enemy.add(enemys)
                    else:
                        enemy_list = [enemy1, enemy1, enemy1, enemy2, enemy2, enemy2, enemy3, enemy3]
                        # 随机产生多架飞机
                        enemys = random.sample(enemy_list, random.randint(self.step, self.step+2))
                        # 添加到精灵组
                        Resource.group_enemy.add(enemys)

    def update(self):
        """更新场景"""
        Resource.group_resource.update()
        Resource.group_resource.draw(self.screen)

        Resource.group_hero.update()
        Resource.group_hero.draw(self.screen)

        Resource.group_enemy.update()
        Resource.group_enemy.draw(self.screen)

        Resource.group_enemy_bullet.update()
        Resource.group_enemy_bullet.draw(self.screen)

        # 当前游戏状态栏
        self.screen.blit(Resource.font.render(f"血量：{self.hp}", True, (255, 0, 0)), (0, 30))
        self.screen.blit(Resource.font.render(f"分数：{self.score}", True, (255, 0, 0)), (0, 0))
        self.screen.blit(Resource.font.render(f"历史最高分为:{Resource.history_score}", True, (255, 0, 0)), (0, 60))

        # 更新英雄飞机子弹
        Resource.group_hero_bullet.update()
        Resource.group_hero_bullet.draw(self.screen)

        pygame.display.update()

    def update1(self):
        """跳转场景更新"""
        Resource.group_jump.update()
        Resource.group_jump.draw(self.screen)

        pygame.display.update()

    def collide(self):
        """碰撞检测"""
        # 英雄飞机子弹 vs 敌人飞机
        for enemy in Resource.group_enemy:
            res = pygame.sprite.groupcollide(Resource.group_hero_bullet, Resource.group_enemy, True, False,
                                             collided=pygame.sprite.collide_rect)
            if len(res.keys()) > 0:
                enemy.hp -= 1
                if enemy.hp == 0:
                    enemy.kill()
                    self.score += enemy.integral
                    print("========", self.score)

            # 英雄飞机 vs 敌人飞机
            res = pygame.sprite.groupcollide(Resource.group_hero, Resource.group_enemy, False, True,
                                             collided=pygame.sprite.collide_rect)
            if len(res.keys()) > 0:
                self.hp -= 1
                pygame.mixer.music.load("sound/game_over.ogg")
                pygame.mixer.music.play(1)
                for hero in Resource.group_hero:
                    hero.rect.x = Resource.screen_rect.centerx - 60
                    hero.rect.y = Resource.screen_rect.centery + 240
                if self.hp == 0:

                    self.dead_frame()

        # 子弹碰撞
        pygame.sprite.groupcollide(Resource.group_enemy_bullet, Resource.group_hero_bullet, True, True)
        # 敌人子弹与英雄飞机碰撞
        a = pygame.sprite.groupcollide(Resource.group_enemy_bullet, Resource.group_hero, True, False)
        if len(a.keys()) > 0:
            self.hp -= 1
            pygame.mixer.music.load("sound/game_over.ogg")
            pygame.mixer.music.play(1)
            for hero in Resource.group_hero:
                hero.rect.x = Resource.screen_rect.centerx - 60
                hero.rect.y = Resource.screen_rect.centery + 240
            if self.hp == 0:
                self.dead_frame()

    def dead_frame(self):
        self.update_history()
        pygame.mixer.music.stop()
        """死亡后分数显示"""
        dead = Dead(Resource.jump_images[self.step-1], self.screen, self.score)
        while True:
            dead.display()
            if Resource.is_play:
                pass
            else:
                self.hp = 3
                self.score = 0
                self.step = 1
                Resource.group_hero_bullet.empty()
                Resource.group_hero.empty()
                Resource.group_enemy.empty()
                Resource.group_enemy_bullet.empty()
                Resource.group_resource.empty()
                Resource.group_jump.empty()
                return self.run()
            pygame.display.update()

    def update_history(self, path="score.txt"):
        """更新历史分数"""
        if os.path.exists(path):
            if self.score > Resource.history_score:
                with open(path, "w") as file:
                    file.write(str(self.score))

    def read_history(self, path="score.txt"):
        """读取历史分数"""
        if os.path.exists(path):
            with open(path, "r") as file:
                Resource.history_score = int(file.read())
        else:
            with open(path, "w") as file:
                file.write("0")


engine = Engine()


engine.run()
