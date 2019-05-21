class Node:
    """'节点"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Link:
    """双链表"""
    def __init__(self, node = None):
        self._head = node

    def is_empty(self):
        """是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while None != cur:
            cur = cur.next
            count += 1
        return count

    def iternodes(self):
        """遍历整个链表"""
        cur = self._head
        while None != cur:
            print(cur.data, end = '  ')
            cur = cur.next
        print()
    def append(self, data):
        """链表尾部添加元素"""
        node = Node(data)  # 把值转为节点对象
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while None != cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur
    def insert(self, pos, data):
        """在指定位置添加元素"""
        node = Node(data)
        if pos > self.length():
            self.append(data)
        else:
            per = self._head
            count = 0
            while count < pos:
                count += 1
                per = per.next
            #   循环结后per指向pos位置
            node.next = per
            node.prev = per.prev
            per.prev.next = node
            per.prev = node
    def remove(self, data):
        """删除节点"""
        cur = self._head
        while None != cur:
            if cur.elem == data:
                # 处理删除节点是头结点的情况
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:   # 只有一个元素
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
ll = Link()
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.insert(3, 'a')
# ll.remove('a')
ll.iternodes()