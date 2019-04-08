import re
result = re.findall(r'\bhello\b|\bworld\b|\bhi\b', 'hello world hi world')
print(result)
result = re.match(r'.*?@.*?.com', '4324342@qq.com')
print(result)
result = re.match(r'(.*?)@(.*?)(.com)', '4324342@qq.com')
print(result.group(), result.group(1), result.group(2), result.group(3))
result = re.match(r'(hello).*?\1', 'hello world hello china')
print(result.group(), result.group(1))
