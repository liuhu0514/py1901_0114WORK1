def rename(classname, parentclass, attrs):
    newclassname = 'new'+classname
    newattrs = {}
    for k, v in attrs.items():
        if not k.startswith("__"):
            key = k+"attr"
            newattrs[key] = v
    return type(newclassname, parentclass, newattrs)


class Goods(metaclass=rename):
    name = None
    age = None


print(Goods.__name__)
print(Goods.__dict__)
