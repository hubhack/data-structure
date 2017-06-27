# the binary Tree : 二叉树, 每个节点最多只两个节点

class _BinTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None







# 三种depth-first遍历
def preorderTrav(subtree):
    """先根遍历"""
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)

def inorderTrav(subtree):
    """ 中根遍历"""
    if subtree is not None:
        preorderTrav(subtree.left)
        print(subtree.data)
        preorderTrav(subtree.right)

def psotorderTrav(subtree):
    """ 后根遍历"""
    if subtree is not None:
        preorderTrav(subtree.left)
        print(subtree.data)
        preorderTrav(subtree.right)

# 宽度优先遍历(bradth-First, Traversal)
def breadthFirstTrav(bintree):
    from queue import Queue
    q = Queue()
    q.put(bintree)
    while not q.empty():
        node = q.get()
        print(node.data)
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)

class _ExpTreeNode:
    __slots__ = ('element', 'left', 'right')

    def __init__(self,data):
        self.element = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '<_ExpTreeNode:{}{}{}>'.format(
            self.element, self.left, self.right)



from queue import Queue
class ExpressionTree:
    def __int__(self, expStr):
        self._expTree = None
        self._buildTree(expStr)

    def evaluate(self, varDict):
        return self._evalTree(self._expTree, varDict)

    def __str__(self):
        return self._buildString(self._expTree)


    def _buildString(self, treeNode):
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.element)

        else:
            expStr = '('
            expStr += self._buildString(treeNode.left)
            expStr += str(treeNode.element)
            expStr += self._buildString(treeNode.right)
            expStr += ')'
            return expStr

    def _evalTree(self, subtree, varDict):
        # 是不是叶子节点, 是的话说明是操作数，直接返回
        if subtree.left is None and subtree.right is None:
            # 操作数是合法数字吗
            if subtree.element >= '0' and subtree.element <= '9':
                return int(subtree.element)
            else:  # 操作数是个变量
                assert subtree.element in varDict, 'invalid variable.'
                return varDict[subtree.element]
        else:  # 操作符则计算其子表达式
            lvalue = self._evalTree(subtree.left, varDict)
            rvalue = self._evalTree(subtree.right, varDict)
            print(subtree.element)
            return self._computeOp(lvalue, subtree.element, rvalue)

    def _computeOp(self, left, op, right):
        assert op
        op_func = {
            '+': lambda left, right: left + right,  # or import operator, operator.add
            '-': lambda left, right: left - right,
            '*': lambda left, right: left * right,
            '/': lambda left, right: left / right,
            '%': lambda left, right: left % right,
        }
        return op_func[op](left, right)

    def _buildTree(self, expStr):
        expQ = Queue()
        for token in expStr:  # 遍历表达式字符串的每个字符
            expQ.put(token)
        self._expTree = _ExpTreeNode(None)  # 创建root节点
        self._recBuildTree(self._expTree, expQ)

    def _recBuildTree(self, curNode, expQ):
        token = expQ.get()
        if token == '(':
            curNode.left = _ExpTreeNode(None)
            self._recBuildTree(curNode.left, expQ)

            # next token will be an operator: + = * / %
            curNode.element = expQ.get()
            curNode.right = _ExpTreeNode(None)
            self._recBuildTree(curNode.right, expQ)

            # the next token will be ')', remmove it
            expQ.get()

        else:  # the token is a digit that has to be converted to an int.
            curNode.element = token

vars = {'a': 5, 'b': 12}
expTree = ExpressionTree("((2*7)+8)")
print(expTree)
print('The result = ', expTree.evaluate(vars))








