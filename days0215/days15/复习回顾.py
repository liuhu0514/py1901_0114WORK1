'''
python类型中
    如果属性是普通数据：
        set:设置数据
        get:获取数据
    问题1：如果属性是字典【组合数据类型】:
        给属性设置数据 set
        获取属性的数据 get
        给属性添加数据
        从属性中删除数据
    问题2：
         菜单选项字典中使用了系统类型的用户字典，修改不了？

    问题3：
        属性声明位置：__init__()内部：成员属性：每个对象的数据都是独立
        属性声明在类型的外部？
        属性声明在类型的内部，但是声明在方法的外部？
'''
"""
 问题1：如果属性是字典：怎么设置它的如下几个方法
    set方法
    get方法
    添加数据的方法
    删除数据的方法
    
    方法：技术上的实现~保障技术完整性
    方法：业务上的实现~保障业务流程正确性
"""
class Core:
    """核心系统类型"""

    def __init__(self):
        self.__users = dict()

    # 技术上的实现：set/get完成封装操作
    def set_users(self, users):
        self.__users = users

    def get_users(self):
        return self.__users

    # 业务上的实现
    def add_user(self, user):
        self.__users[user.username] = user

    def find_user(self, username):
        return self.__users.get(username)

    def delete_user(self, username):
        self.__users.pop(username)

    def lock_user(self, username):
        user = self.find_user(username) # 推荐 find_user中不一定只有一行代码
        # user = self.__users.get(username) # 不推荐：

        # user.is_active = False
        user.set_active(False)

    def unlock_user(self, username):
        user = self.find_user(username)
        # user.is_active = True
        user.set_active(True)


    # 业务上的实现：实现用户对象数据丶添加、删除
"""
如果是系统功能的：注册(添加用户对象)、登录(查询用户对象)、注销(删除用户对象)
    由于users字典就是当前类型的，所以可以直接通过self.users进行操作。
管理员对象：Manager
    管理员可以直接添加一个会员账号、可以直接删除一个会员账号
    管理员类型中获取所有用户字典：core.users-> core.get_users()
    
    【不推荐】管理员类型中操作用户字典：core.get_users()['admin'] = user
                            core.get_users().pop('admin')
         获取所有用户字典、操作用户字典中的数据 【两个功能 混合 到一起】
    【店家推荐】业务操作，应该提供操作方法
        管理员添加一个会员账号：core.add_user(user)
        管理员查看一个会员信息：core.find_user(username)
        管理员删除一个会员信息：core.delete_user(username)
        管理员锁定一个会员账号：core.lock_user(username)
    
"""

"""
问题2：对象数据的操作出现了冲突
    有一些对象~在系统运行过程中，只能有一个！如系统类型对象
    任务：既然~有一种类型创建的对象在项目中只能有一个！
        开发这样一个类型，只能创建一个对象！【单例模式】
"""
class Core1:

    def __init__(self):
        self.name = "tom"


# 创建对象
core = Core1()
print(core.name) # tom
core.name = "jerry"
print(core.name) # jerry

# 该对象要使用在其他地方
d = {'core': Core1()}
# d = {'core': core}
print(d.get('core').name) # ? tom


"""
问题3：属性声明位置：
    1. 已知：属性声明在__init__()方法中，成员属性，每个创建的对象 这些属性数据独立的。
    2. 属性声明在类型中，方法外。所有对象都能访问但是不能直接修改的数据。   
        专门定义所有对象访问的公共数据
    3. 属性{不能称为属性~变量}声明在类型外部！全局变量
        任何类型创建的对象都能访问的数据。
        
    成员属性[对象]-> 类属性[当前类型的所有对象]-> 全局变量[所有对象]
"""
class Person:
    # 类属性
    max_age = 150

    def __init__(self, name):
        # 成员属性
        self.name = name
        self.age = 150


# 成员属性：成员~对象，成员属性就是对象的属性，每个对象的属性数据都是互相独立的。
p1 = Person("tom")
p2 = Person("jerry")
print(p1.name)# tom
print(p2.name)# jerry

#
print(p1.max_age)
print(p2.max_age)

# 类属性，由该类创建的所有对象都可以访问，但是不能修改
# p1.age = 120 # 扩展属性
# print(p1.max_age)
# print(p2.max_age)

# 类型可以修改类属性，影响所有对象的访问结果
Person.max_age = 120
print(p1.max_age)
print(p2.max_age)

# 类属性：为什么可以让类型修改，不能让对象修改？
# 面试题~类型可以创建属于该类型的所有对象，类型可以修改影响所有对象的类属性数据。
    # 对象和对象之间的数据都是独立的，对象不能操作影响其他对象的数据，类属性就是这样的数据。
