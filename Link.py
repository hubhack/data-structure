class Node:
    def __init__(self, data):
        self.data = data
        self.p = None

class Link():
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self._head = node
        else:
            #  不是空,则找到尾部,将我不结点指向新结点
            cur = self._head
            while cur.p is not None:
                cur = cur.p
            cur.p = node
    def iternodes(self):
        '''遍历'''
        cur = self._head
        print(cur.data)
        while cur is not None:
            yield cur.data
            cur = cur.p
link_list = Link()
link_list.append(7)
link_list.append(3)
link_list.append(5)
link_list.append(4)
for i in link_list.iternodes():
    print(i, end='\t')
# print(id(7))