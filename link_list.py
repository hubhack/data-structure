'''用面向对象实现Linkedlist链表
单链表实现append. iternodes方法
双向链表实现append, pop, insert, remove, iternodes方法
思路: 定义两个类, 一个结点类,一个link类, '''
# HEAD ->    data-> p -> data -> p  [5, 7, 3, 4]
# p 为列表的索引 5    1     7      2
# list.append()
list()
lst = [5, 7, 3, 4]
class Link(list):
    def __init__(self, *args):
        super().__init__(*args)
        for i in range(len(self)):
            self[i] = (self[i], i+1)
    def append(self, *args):
        _length = len(self)
        NUll = None
        self[-1] = (*args, NUll)
    def iternodes(self):
        yield


l = Link(lst)
print(l)
# l.iternodes()
l.append(6)
l.append(6)
print(l)

