"""
实现给宠物去宠物医院去看病
"""


class Pet:
    """
    创建一个宠物类型
    """
    def __init__(self, name, health):
        """
        宠物类型初始化属性
        :param name: 宠物名称
        :param health: 宠物健康值
        """
        self.name = name
        self.health = health

    def recovery(self):
        """
        宠物康复情况的行为
        :return: 无
        """
        self.health += 5
        print(self.name, "宠物正在康复中...")


class Person:
    """
    创建一个人的类型
    """
    def __init__(self, name, health):
        """
        初始化人的属性
        :param name: 人的名字
        :param health: 人的健康值
        """
        self.name = name
        self.health = health

    def recovery(self):
        """
        人康复的行为
        :return: 无
        """
        self.health += 8
        print(self.name, "正在康复中...")


class Hospital:
    """
    创建一个医院类型
    """
    def __init__(self, name):
        """
        初始化医院的属性
        :param name: 医院名称
        """
        self.name = name

    def treat(self, pet):
        """
        医院治疗的行为
        :return: 无
        """
        print("欢迎来到%sHospital" % self.name)
        if isinstance(pet, Pet):
            while pet.health <= 65:
                print("正在给宠物%s治疗中..." % pet.name)
                pet.recovery()
            else:
                print("宠物%s已经健康了..." % pet.name)

        else:
            print("这是宠物医院，不给其他生物治疗，请换一家医院，感谢您的理解！")


# 创建一个宠物对象
pet1 = Pet("Tom", 45)

# 创建一个医院
hospital = Hospital("宠物之家")

# 调用医院治疗的行为
hospital.treat(pet1)

person = Person("老刘", 60)
hospital.treat(person)
