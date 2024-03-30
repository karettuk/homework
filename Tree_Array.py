class BinaryTree :
    def __init__(self) :
        self.items = []

    def setData(self, item) :
        if len(self.items) == 0 :
            self.items.append(None)  #완전 이진 트리 공식 쓸려고 0번 인덱스 공백으로 지정!
        
        self.items.append(item)

    def getLeftSubTree(self, item) :
        idx = self.items.index(item)    #index(item) -> item의 인덱스 숫자 구해줘
        if len(self.items) >= 2*idx :
            return self.items[2*idx]

    def getRightSubTree(self, item) :
        idx = self.items.index(item)
        if len(self.items) >= 2*idx+1 :
            return self.items[2*idx+1]

    def getParentNode(self,item) :
        idx = self.items.index(item)
        if len(self.items) >= idx//2 :
            return self.items[idx//2]

    def printTree(self) :
        print('------------------------------')
        for k in range(1,len(self.items)) :
            print(self.items[k], end=' ')
        print()
        print('------------------------------')


if __name__ == '__main__' :
    bt = BinaryTree()
    bt.setData(9)
    bt.setData(6)
    bt.setData(3)
    bt.setData(7)
    bt.setData(4)
    bt.setData(2)
    bt.setData(5)
    bt.setData(1)
    bt.setData(8)
    bt.printTree()
    print[bt.getLeftSubTree(4)]
    