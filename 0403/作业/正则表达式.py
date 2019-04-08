import re

# list1 = ['hello', 'python', 'pyinfo', 'apple', 'china']
# s = []
# for l in list1:
#     if l[0:2] == 'py':
#         s.append(l)
# print(s)
# a = 'aksd345ksd23fsd232'
# m = r'[0-9]+'
# num = re.findall(m, a)
# print(num)

strl = 'hello world'
m = 'hello w'
ms = re.match(m, strl)
print(ms)
print(ms.span())
