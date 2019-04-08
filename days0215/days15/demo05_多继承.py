"""
python中的多继承
    体现的是什么样的编程思想：一个对象在不同场景中，可能扮演不同的角色【设计时多态】
"""


class Son:

    def xiao_shun(self):
        print("百善孝为先")


class Student:

    def xue_xi(self):
        print("好好学习，天天向上")


class Friend:

    def play(self):
        print("吃喝玩乐.....")


class Person(Son, Student, Friend):
    """人的类型：继承儿子、学生、朋友"""
    pass


p = Person()
# 家庭环境
if isinstance(p, Son):
    p.xiao_shun()

# 学习环境中
if isinstance(p, Student):
    p.xue_xi()

# 朋友
if isinstance(p, Friend):
    p.play()


def xue_tang(person):
    # 作为一个学员，在教室要好好学习
    if isinstance(person, Student):
        # person.play()
        person.xue_xi()


xue_tang(p)
