def rename(classname, parentclass, attrs):
    newattrs = {}
    for k, v in attrs.items():
        if not k.startswith("__"):
            k = classname.lower()[0]+'_'+k
            newattrs[k] = v
    return type(classname, parentclass, newattrs)


class Good(metaclass=rename):
    name = None
    age = None

    def __init__(self):
        self.sex = None


g = Good()
print(hasattr(g, 'name'))
print(hasattr(g, 'age'))
print(g.__class__)
print(Good.__dict__)
print(g.__dict__)
