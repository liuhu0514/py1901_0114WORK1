'''
普通文件操作方式
    1. 文本文件写入
    2. 文本文件的读取

    3. 二进制文件的操作
'''
# 1. 将程序中的数据，写入到文件中
file = open('./data/1.1.text', 'w', encoding='UTF-8')
# 程序中有一个字符串
message = 'hello 世界'
# 将数据写入到文件中
file.write(message)
# 关闭文件
file.close()

# 2. 将文件中的数据，读取到程序中
# 按照只读的方式打开文件
# file = open(file='./data/1.1.text', mode='r', encoding='utf-8')
# # 从文件中读取数据，展示到控制台中
# info = file.read()
# print(info)
# # 关闭文件
# file.close()

# 2. 文本文件的追加
# file = open(file='./data/1.2.text', mode='a', encoding='UTF-8')
# # 要操作的文本数据
# # message = '人说，林深时见鹿，海蓝时见鲸，夜深时见你.'
# # file.write(message)
#
# # message2 = "\n但是，林深时雾起，海蓝时浪涌，夜神时梦续.\n"
# # file.write(message2)
#
# # message3 = "\r\n你可知：鹿踏雾而来，鲸随浪而起，你未曾转身，怎知我已到来..\r\n"
# # file.write(message3)
#
# # 关闭文件
# file.close()

# 4. 二进制文件的操作
# 'E:/WORK_IMG/lihen/a.jpg'
# 读取计算机中的二进制文件数据
file = open(file='E:/WORK_IMG/lihen/a.jpg', mode='rb')
# 读取数据到程序中
# 双引号字符串前面有个字母b表示是二进制数据、字母u表示Unicode数据
# \x开头的是十六进制数据、\o开头的是八进制数据
# print(file.read())

# 将数据重新存储到我们指定的位置
# file2 = open(file='./data/test.jpg', mode='wb')
# file2.write(file.read())
# # 关闭文件2
# file2.close()

# 关闭文件
file.close()

# 5. 重要：文件的快捷操作：with语法
with open('E:/WORK_IMG/lihen/a (20).JPG', 'rb') as file1:
    # 打开文件，将文件对象赋值给变量file1，with中的代码执行完成，文件file1自动关闭
    with open('./data/' + file1.name[file1.name.rfind('/'):], 'wb') as file2:
        # 将读取的文件存储到指定的文件夹中
        file2.write(file1.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'E:/WORK_IMG/lihen/a(71).jpg'
# 文件没有发现你的错误  [错误代号：2]

'''

字符串可以切片操作：

s1 = "hello worl"
      0123456789
s1[start:stop:step]
s1[1:] -> 123456789 -> ello worl
s1[1:3]-> 12 -> el
s1[1:9:2] -> 'el o'
s1[1::2] -> 'el ol'
s1[::-1] -> 字符串翻转
    s1 = "lrow olleh"
          9876543210
         -1
s1[3:1:-1] -> ll
s1[-1:-3:-1]-> lr
'''
