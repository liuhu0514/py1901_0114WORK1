import re
s1 = 'hello world'
# result = re.match('he', s1)
# result = re.search('l', s1)
# result = re.fullmatch('hello world', s1)
# result = re.findall('l', s1)
# result = re.split('l', s1)
# result = re.sub('l', '666', s1)
# result = re.finditer('l', s1)
result = re.compile('he')

if result:
    print(result, type(result))
    print(dir(result))
    # for r in result:
    #     print(r, type(r))

    # print(result, type(result))
    # # print(result.span(), result.group())
    # print(dir(result))
