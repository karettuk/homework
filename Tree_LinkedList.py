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

    def levelorder(self, root) :
        q = []
        q.append(root)
        while len(q) != 0 :
            node = q.pop(0)
            print(node.value, end=' ')
            if node.left != None : 
                q.append(node.left)
            if node.right != None :
                q.append(node.right)
        print()