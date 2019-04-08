import re
# ^匹配字符串开头字符
result = re.findall('^hello', 'hello world hello zhengzhou')
print(result)
# $匹配字符串结尾
result = re.findall('zhengzhou$', 'hello world hello zhengzhou')
print(result)
# \b判断一个单词的边界
result = re.findall(r'\bhello\b', 'hello world hello zhengzhou')
print(result)
# \B匹配非单词边界
result = re.findall(r'\Bhello\B', 'hello world hello zhenghellozhou')
print(result)

