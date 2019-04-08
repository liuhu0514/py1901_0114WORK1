import re
result = re.findall('.', 'hello world', flags=re.M)
print(result)

result = re.findall('[a-hw]', 'hello world', flags=re.M)
print(result)

result1 = re.findall('\d[.]', 'kdsf3j43 fsfd5')
print(result1)

result = re.findall('\D', 'lsk5sfsd34545klf')
print(result)
