# 双向链表
class SingleNode:
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.next = next
        self.prev = prev
    def __repr__(self):
        return repr(self.item)
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.items = []

    def append(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.items.append(node)
    def insert(self, index, item):
        if index < 0:
            raise ValueError
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:
            self.append(item)
            return
        node = SingleNode(item)
        prev = current.prev
        if prev is None:
            self.head = node
        else:
            prev.next = node
            node.prev = prev
        node.next = current
        current.prev = node
        self.items.insert(index, node)
    def pop(self):
        if self.tail is None:
            raise Exception

        node = self.tail
        item = node.item
        prev = node.prev
        if prev is None:
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev

        self.items.pop()
        return item
    def remove(self, index):
        if self.tail is None:
            raise Exception
        if index < 0:
            raise ValueError
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:
            raise ValueError
        prev = current.prev
        next = current.next
        if prev is None and next  is None :
            self.head = None
            self.tail = None
        elif prev is None:
            self.head  = next
            self.prev = None
        elif next is None:
            self.tail = prev
            prev.next = None
        else:
            prev.next = next
            next.prev = prev
        del current
        self.items.pop(index)
    def iternodes(self, reverse = False):
        current = self.tail if reverse else self.head
        while current:

            yield current

            current = current.prev if reverse else current.next

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, value):
        node = self[index]
        node.item = value

    def __iter__(self):
        return self.iternodes()
a = LinkedList()

a.append(3)
a.append(3)
a.append(3)

print(list(a.iternodes()))