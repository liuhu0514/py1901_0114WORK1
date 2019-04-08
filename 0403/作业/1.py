"""
父子类相互调用：子类可以调用父类中的方法
    父类可以直接调用父类的方法
"""


def getinfo(self):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%')


def getname(self):
    print('name_name_name_name_name_name_name_name')


Goods = type('Goods', (), {'id': '1', 'name': 'lh', 'getinfo': getinfo})
Food = type('Food', (Goods,), {'type': None, 'getname': getname})
g1 = Goods()
f1 = Food()

g1.getinfo()
f1.getinfo()  # 子类可以调用父类方法
f1.getname()
