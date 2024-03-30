class Heap :
    def __init__(self) :
        self.items = []

    def setData(self, item):
        a = item
        if len(self.items) == 0 :
            self.items.append(None)  #완전 이진 트리 공식 쓸려고 0번 인덱스 공백으로 지정!
        self.items.append(a)
        try :  #ParentNode 없을 수도 있으니
            while len(self.getParentNode(a)) < len(a):
                idx = self.items.index(a)
                self.items[idx//2], self.items[idx] = self.items[idx], self.items[idx//2]
        except: pass
        
    def dele(self):
        if len(self.items) <= 1:   #맨 앞 None만 남은 경우
            print("삭제할 데이터가 없습니다.")
        elif len(self.items) == 2: #Left, Right 없는 경우
            self.items.pop()
        else :                     #그 외
            self.items[1] = self.items.pop()
            a = self.items[1]
            b = True
            while b:
                idx = self.items.index(a)                                 #왼쪽이 크냐, 오른쪽이 크냐 판단
                if len(self.getLeftSubTree(a)) < len(self.getRightSubTree(a)):
                    c = self.getRightSubTree(a)
                    idx_C = 2*idx+1
                else : 
                    c = self.getLeftSubTree(a)
                    idx_C = 2*idx
                
                #전환
                if len(a)<len(c):
                    self.items[idx], self.items[idx_C] = self.items[idx_C], self.items[idx]
                else : b = False

    def getLeftSubTree(self, item) :
        idx = self.items.index(item) 
        if len(self.items)-1 >= 2*idx :       #수정(함수 리턴값이 없는 예외경우를 만들지 않기 위해)
            return self.items[2*idx]
        else : return ""

    def getRightSubTree(self, item) :
        idx = self.items.index(item)
        if len(self.items)-1 >= 2*idx+1 :
            return self.items[2*idx+1]
        else : return ""

    def getParentNode(self,item) :
        idx = self.items.index(item)
        if len(self.items)-1 >= idx//2 :
            return self.items[idx//2]
        else : return ""

    def printHeap(self) :
        print('------------------------------')
        for _ in range(len(self.items)-1):    
            print(self.items[1])
            self.dele()
        print('------------------------------')

heap = Heap()
try :
    num = int(input("기사 개수 : "))
    if num <= 0:
        raise Exception
except :
    print("자연수를 입력해주세요")
    exit()
for _ in range(num):
    title = str(input("기사 제목:"))
    heap.setData(title)
heap.printHeap()