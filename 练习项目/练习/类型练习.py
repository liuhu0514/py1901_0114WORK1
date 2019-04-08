users = dict()


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self, food):
        print("%s该吃饭了，吃%s" % (self.name, food))


a = input("姓名")
b = input("年龄")
c = input("性别")

p1 = Person(a, b, c)
user = {"admin": a, "age": b, "gender": c}
users[a] = user
print("姓名：",p1.name,"年龄：", p1.age,"性别：", p1.gender)
p1.eat("烤鸭")
