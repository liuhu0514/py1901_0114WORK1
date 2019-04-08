#飞机大战 的 分析

#开始界面
#       背景  标题    底部动图   开始按钮
#   开始界面类：
#         属性： 图片集合   屏幕   位置
#         方法:  显示


#游戏界面
#
#   背景类：
#          属性 : 图片  屏幕   位置   速度
#          方法:  显示
#   主角类：
#          属性：图片   屏幕   位置   速度  血量
#          方法： 显示   控制  产生子弹   死亡
#   敌机类：
#          属性：图片   屏幕   位置   速度  血量  标签
#          方法：显示  移动  死亡
#   敌机工厂类：
#          产生敌机
#   子弹类：
#         属性：图片   屏幕   位置   速度
#         方法: 显示   移动   碰撞
#
#
#   道具类：
#   分数类：


import pygame
import random,sys,os,math

#开始界面图片
startImgs=[pygame.image.load("plane/image/background.png"),
pygame.image.load("plane/image/name.png"),
pygame.transform.scale(pygame.image.load("plane/image/loading.png"),(480,480)),
pygame.image.load("plane/image/icon72x72.png")
           ]
#开始界面下部三张图
startThreeImgs=[
    pygame.image.load("plane/image/game_loading1.png"),
    pygame.image.load("plane/image/game_loading2.png"),
    pygame.image.load("plane/image/game_loading3.png")
]

#开始界面类
class StartPanel:
    #类变量
    isIn=False #鼠标是否在 按钮里
    #开始界面类：
    #    属性： 图片集合   屏幕   位置
    #    方法:  显示
    def __init__(self,imgs,threeImgs,screen) -> None:
        self.imgs=imgs
        self.threeImgs=threeImgs
        self.screen=screen
        #sin变量
        self.sinY=0
        #底部三张图 的索引
        self.threeIndex=0
        # 累加变量
        self.addThree=0
    def Display(self):
        #背景
        self.screen.blit(self.imgs[0],(0,0))
        #标题
        self.sinY+=0.1
        if self.sinY==100:
            self.sinY=0
        self.screen.blit(self.imgs[1],(25,100+50*math.sin(self.sinY)))
        #圆环
        self.screen.blit(self.imgs[2], (0, 100))
        #按钮
        x=self.screen.blit(self.imgs[3], (200, 300))
        #类属性访问方法，【类名.变量名】
        StartPanel.isIn=x.collidepoint(pygame.mouse.get_pos())
        #底部三张图
        self.screen.blit(self.threeImgs[self.threeIndex],(150,600))
        self.addThree+=1
        if  self.addThree==20: #累加变量  1 加到20   再替换一张图
            self.threeIndex+=1
            if self.threeIndex==3:
                self.threeIndex=0
            self.addThree=0

#***************************************
#初始化pygame
pygame.init()

#设置窗口大小
screen=pygame.display.set_mode((480,700))

#背景音乐
pygame.mixer.music.load("plane/sound/game_music.mp3")
pygame.mixer.music.play()

#开始界面对象
startPanel=StartPanel(startImgs,startThreeImgs,screen)


#游戏是否开始
isPlay=False  #False没开始


#所有事件 监测
def AllEvent():
    global  isPlay
    # 事件监测
    for i in pygame.event.get():
        # 退出事件
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 鼠标事件
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if StartPanel.isIn==1:
                    print("开始游戏！")
                    isPlay=True
        #键盘事件
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_ESCAPE:
                isPlay=False
#主函数
def Main():
    while True:
        #事件监测
        AllEvent()

        #填充背景颜色
        screen.fill(pygame.Color("red"))

        if isPlay:
            #游戏界面
            pass
        else:
            #开始界面显示
            startPanel.Display()

        #刷新屏幕
        pygame.display.update()


if __name__ == '__main__':
    Main()

