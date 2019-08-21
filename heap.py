# Heap(堆):二叉树最直接的一个应用就是是实现堆.堆就是一颗完全二叉树, 最大堆的非叶子节点的值都比孩子大, 
# 最小堆的非叶子节点的值都比孩子小, python内置了heapq模块帮助我们实现堆操作,比如用内置的heapq模块实现了堆排序.
# 使用python内置和heapq实现heap sort
def heapsort(iterable):
    from heapq import heappush, heappop
    h = []
    for value in iterable:
        heappush(h, value)
        
    return [heappop(h) for i in range(len(h))]
# 但是一般实现堆的时候实际上下并不是用数节点来实现, 而是使用数组实现, 效率比较高, 为什么
# 可以用数组实现, 因为完全二叉树的性质, 可以用下标之间的关系表示节点之间的关系.
