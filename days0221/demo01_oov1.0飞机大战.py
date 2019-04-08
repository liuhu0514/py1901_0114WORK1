"""
飞机大战OO_v1.0

"""
import pygame, random


class GameSprite(pygame.sprite.Sprite):
    """自定义游戏精灵"""

    def __init__(self, image_path, speed=1, x=0, y=0):
        """自定义初始化游戏精灵数据"""
        super().__init__()
        # 资源图片
        self.image = pygame.image.load(image_path)
        # 资源尺寸
        self.rect = self.image.get_rect()
        # 运动速度
        self.speed = speed
        # 初始化坐标
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """更新"""
        # 默认事件控制
        self.event()
        # 默认运动
        self.move()

    def event(self):
        """事件操作"""
        # 退出事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 判断是否退出
                if event.type == pygame.QUIT:
                    # 游戏退出
                    pygame.quit()
                    exit()

                # 创建敌方飞机的事件
                if event.type == ENEMY_EVENT_CREAET:
                    # 创建敌方飞机
                    enemy = EnemySprite("images/enemy/Enemy3.png", random.randint(3, 6))
                    enemy1 = EnemySprite("images/enemy/Enemy4.png", random.randint(2, 3))
                    enemys = [enemy, enemy1, enemy, enemy, enemy, enemy1]
                    # 产生随机数量的飞机
                    a = random.sample(enemys, random.randint(1, 3))
                    # 添加到敌方的飞机精灵组里去
                    group_enemy.add(a)
                    print("敌方飞机出现了")

    def move(self):
        """移动"""
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    """游戏背景精灵"""

    def move(self):
        """运动及边界判断"""
        # 调用父类方法，让当前图片运动
        super().move()
        # 添加边界判断
        if self.rect.y > screen_rect.height:
            self.rect.y = -screen_rect.height


class HeroSprite(GameSprite):
    """英雄飞机精灵"""

    def __init__(self, image_path, speed, x, y):
        super().__init__(image_path, speed, x, y)
        self.group_hero_bullet = pygame.sprite.Group()

    def update(self):
        """更新"""
        self.event()
        self.move()

    def event(self):
        """事件控制"""
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_UP]:
            print("飞机向上移动")
            self.rect.y -= self.speed

        elif key_down[pygame.K_DOWN]:
            print("飞机向下移动")
            self.rect.y += self.speed

        elif key_down[pygame.K_LEFT]:
            print("飞机向左移动")
            self.rect.x -= self.speed

        elif key_down[pygame.K_RIGHT]:
            print("飞机向右移动")
            self.rect.x += self.speed

    def move(self):
        """边界判断"""
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.x > screen_rect.width - self.rect.width:
            self.rect.x = screen_rect.width - self.rect.width

        elif self.rect.y < 0:
            self.rect.y = 0

        elif self.rect.y > screen_rect.height - self.rect.height:
            self.rect.y = screen_rect.height - self.rect.height


class BulletSprite(GameSprite):
    """子弹精灵类型"""
    def move(self):
        """移动及边界"""
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


class EnemySprite(GameSprite):
    """敌方飞机精灵类型"""
    def __init__(self, image_path, speed):
        super(EnemySprite, self).__init__(image_path, speed)
        # 随机横坐标和纵坐标
        self.rect.x = random.randint(0, screen_rect.width-self.rect.width)
        self.rect.y = -self.rect.height

    def move(self):
        """敌机移动及边界判断"""
        self.rect.y += self.speed
        # 判断边界
        if self.rect.y > screen_rect.height:
            # 移除自己
            self.kill()


# 游戏初始化
pygame.init()

# 添加一个敌方飞机创建事件
ENEMY_EVENT_CREAET = pygame.USEREVENT
# 添加一个计时器，触发创建事件
pygame.time.set_timer(ENEMY_EVENT_CREAET, random.randint(1000, 3000))

# 场景初始化
screen_rect = pygame.Rect(0, 0, 512, 768)
screen = pygame.display.set_mode((screen_rect.width, screen_rect.height), 0, 32)


# 定义背景精灵对象
bg1 = BackgroundSprite("images/bg/step1.jpg")
bg2 = BackgroundSprite("images/bg/step1.jpg")
bg2.rect.y = -bg2.rect.height


# 定义一个英雄飞机精灵对象
hero = HeroSprite("images/hero/hero.png", speed=5, x=screen_rect.centerx-60, y=screen_rect.centery+250)

# 定义初始化资源精灵组
group_init_resource = pygame.sprite.Group(bg1, bg2)

# 创建一个英雄精灵组
group_hero = pygame.sprite.Group(hero)

# 创建一个子弹精灵组
group_hero_bullet = pygame.sprite.Group()
bullet_index = 0

# 创建敌方精灵组
group_enemy = pygame.sprite.Group()

# 创建一个时钟对象
clock = pygame.time.Clock()

# 场景循环
while True:
    # 刷新频率
    clock.tick(60)

    bullet_index += 1
    if bullet_index >= 100:
        bullet_index = 0

    if bullet_index % 20 == 0:
        # 自动发射子弹：创建子弹
        bullet = BulletSprite("images/bullet/bullet2.png", 5, hero.rect.centerx-35, hero.rect.y-40)
        # 子弹添加到精灵组
        group_hero_bullet.add(bullet)

    # 更新资源精灵组
    group_init_resource.update()
    group_init_resource.draw(screen)

    # 更新英雄飞机精灵组
    group_hero.update()
    group_hero.draw(screen)

    # 更新子弹精灵组
    group_hero_bullet.update()
    group_hero_bullet.draw(screen)

    # 刷新敌方飞机的精灵组
    group_enemy.update()
    group_enemy.draw(screen)

    # 子弹和敌方飞机碰撞检测
    pygame.sprite.groupcollide(group_enemy, group_hero_bullet, True, True)

    # 英雄飞机精灵和敌方飞机碰撞
    if pygame.sprite.groupcollide(group_hero, group_enemy, True, True):
        pygame.display.quit()


    # 场景更新
    pygame.display.update()
