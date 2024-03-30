class Stack :
    def __init__(self, c=256) :
        self.items = [None]*c
        self.capacity = c
        self.top = 0

    def push(self, item) :
        if self.capacity > self.top :
            self.items[self.top] = item
            self.top += 1
        else :
            print('stack is full')

    def pop(self) :
        if self.top != 0 :
            self.top -= 1
            return self.items[self.top]
        else :
            print('Stack is empty')

    def peek(self) :
        if self.top != 0 :
            return self.items[self.top-1]
        else :
            print('stack is empty')

    def printStack(self) :
        print('-------------------')
        for i in range(self.top, 0, -1) :
            print(self.items[i-1])
        print('-------------------')
        
    def is_full(self) :
        if self.top == self.capacity :
            return True
        else :
            return False
        
    def is_empty(self) :
        if self.top == 0 :
            return True
        else :
            return False
# stack 끝-------------------------------------------------------------------
#-----------------------------------------------------------------------------

class Node :
    def __init__(self, value, left=None, right=None) :
        self.value = value
        self.left = left
        self.right = right

class BinaryTree :
    def __init__(self) :
        self.root = None
        self.count = 0

    def getData(self, node) :
        return node.value

    def setData(self, node, value) :
        node.value = value

    def makeRootNode(self, node) :
        self.root = node

    def makeLeftSubTree(self, p, c) :
        p.left = c

    def makeRightSubTree(self, p, c) :
        p.right = c

    def getLeftSubTree(self, node) :
        if node != None :
            return node.left

    def getRightSubTree(self, node) :
        if node != None :
            return node.right

    def getHeight(self, root) :
        if root == None :
            return 0

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def preorder(self, node) :
        if node != None :
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node) :
        if node != None :
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def postorder(self, node) :
        if node != None :
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

# 이진트리 끝 ---------------------------------------------------------------
#----------------------------------------------------------------------------

def getPriority(op) :
    if op == '(' or op==')' :
        return 0
    elif op=='+' or op=='-' :
        return 1
    elif op=='*' or op=='/' :
        return 2
    else :
        return -1

def getPostfix(infix) :
    stack = Stack(20)
    
    op = ['+', '-', '*', '/']
    pos = 0
    postfix = ''
    
    for ch in infix :
        if ch in op :
            while stack.is_empty() != True and getPriority(ch) <= getPriority(stack.peek()) :
                postfix += stack.pop()
            stack.push(ch)
        elif ch == '(' :
            stack.push(ch)
        elif ch == ')' :
            while True :
                a = stack.pop()
                if a == '(' :
                    break
                else :
                    postfix += a
        else :
            postfix += ch
        
    #스택에 남아있는 연산자 모두 pop하기
    while stack.is_empty()!=True :
        postfix += stack.pop()
    
    return postfix


def calculator(root) :
    if root == None : return
    
    if root.left == None and root.right == None :
        return int(root.value)
    else :
        n1 = calculator(root.left)
        n2 = calculator(root.right)
        
        if root.value == '+' :
            return n1 + n2
        elif root.value == '-' :
            return n1 - n2
        elif root.value == '*' :
            return n1 * n2
        elif root.value == '/' :
            return n1 / n2
    
    return 0

# 함수 구현 끝 --------------------------------------------------------------
#----------------------------------------------------------------------------

bt = BinaryTree()
n = Node("노르웨이")
bt.makeRootNode(n)
bt.makeLeftSubTree(n,Node("블레도"))