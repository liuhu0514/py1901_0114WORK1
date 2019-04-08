from collections.abc import Iterator, Iterable


class Good:
    def __init__(self, _addr):
        self.addr = _addr
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.addr):
            result = self.addr[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration('越界引发异常')


g = Good(['henan', 'hebei', 'beijing'])
print(isinstance(g, Iterator))
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)
print(isinstance(g, Iterable))
for i in g:
    print(i)
