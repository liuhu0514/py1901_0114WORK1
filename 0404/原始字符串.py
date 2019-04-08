import re
# 匹配失败
result = re.findall("\bhello\b", "hello world hello zhengzhou sayhellook")
print(result)
# 太麻烦
result = re.findall("\\bhello\\b", "hello world hello zhengzhou sayhellook")
print(result)
# 使用原始字符
result = re.findall(r"\bhello\b", "hello world hello zhengzhou sayhellook")
print(result)

