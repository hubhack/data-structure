class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0


    def append(self, item):
        node = Node(item)
        if self.head is None:  # 为空
            self.head = node
            self.tail = node
        else:
            self.tail.next = node  # 链表的尾巴的下一个是node
            node.prev = self.tail  # node的前一个是链表的尾巴
            self.tail = node  # 新的尾巴是node
            self.__size += 1
        return self

    def pop(self):
        if self.head is None:
            raise Exception('Empty')
        else:
            node = self.tail  # 链表的尾部
            item = node.item  # 链表尾部的值
            prev = node.prev  # 链表尾部的前一个
            if prev is None:  # 链表只有一个时
                self.head = None
                self.tail = None
            else:
                self.tail = prev  # 当前尾巴是原尾巴的前一个
                prev.next = None  # 原尾巴的前一个的下一个为None
            self.__size -= 1
            return item

    def iternodes(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def insert(self, index, item):
        if index < 0:
            raise IndexError
        current = None
        for i, nodes in enumerate(self.iternodes()):
            if i == index:
                current = nodes
                break
        else:  # 没有break，没有找到等于index的索引，说明超界了，尾部追加
            self.append(item)
            return

        node = Node(item)
        prev = current.prev
        next = current
        if prev is None:  # index为0时
            self.head = node
            node.next = next
            next.prev = node
        else:
            next.prev = node
            prev.next = node
            node.prev = prev
            node.next = next
        self.__size += 1

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')
        if index < 0:
            raise IndexError
        current = None
        for i, nodes in enumerate(self.iternodes()):
            if i == index:
                current = nodes
                break
        else:  # 没有break，没有找到等于index的索引，说明超界了
            raise IndexError

        prev = current.prev
        next = current.next
        # 有四种情况
        if prev is None and next is None:  # 只有一个时
            self.head = None
            self.tail = None
        elif prev is None:  # index=0时
            self.head = next
            next.prev = None
        elif next is None:  # index是最后一个
            self.tail = prev
            prev.next = None
        else:  # 在中间位置
            prev.next = next
            next.prev = prev
        del current
        self.__size -= 1
    __iter__ = iternodes

ll = Link()
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.insert(3, 'a')
# ll.remove('a')
ll.iternodes()