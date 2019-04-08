"""
给宠物看病
"""


class Pet:
    """
    定义一个宠物类型
    """

    def __init__(self, name, health):
        """
        宠物的属性
        :param name: 宠物名
        :param health: 宠物健康值
        """
        self.name = name
        self.health = health

    def kang_fu(self):
        """
        宠物康复的行为
        :return: 无
        """
        self.health += 5
        print(self.name, "正在康复中...")


class Person:
    """
    定义一个人的类型
    """

    def __init__(self, name, health):
        """
        定义人的属性
        :param name: 人的名称
        """
        self.name = name
        self.health = health

    def kang_fu(self):
        """
        人的康复行为
        :return:
        """

        self.health += 8
        print(self.name, "正在康复中...")


class Hospital:
    """
    定义一个医院类型
    """

    def __init__(self, name):
        """
        医院的属性
        :param name: 医院名
        """

        self.name = name

    def treatment(self, pet):
        """
        医院治疗的行为
        :return:
        """

        if isinstance(pet, Pet):
            while pet.health <= 65:
                print("欢迎来到", self.name, "医院给宠物%s治疗" % pet.name)
                pet.kang_fu()

            else:
                print("宠物%s已经康复..." % pet.name)

        else:
            print("本医院不接受给其他生物治疗，请换一家医院，感谢您的理解...")


pet1 = Pet("Tom", 45)
ht = Hospital("梦之家")
p1 = Person("老刘", 55)
ht.treatment(pet1)
ht.treatment(p1)
