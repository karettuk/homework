class Heap :
    def __init__(self) :
        self.items = []

    def setData(self, item):
        a = item
        if len(self.items) == 0 :
            self.items.append(None)  #완전 이진 트리 공식 쓸려고 0번 인덱스 공백으로 지정!
        self.items.append(a)
        try :  #ParentNode 없을 수도 있으니
            while self.getParentNode(a) < a:
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
                if self.getLeftSubTree(a) < self.getRightSubTree(a):
                    c = self.getRightSubTree(a)
                    idx_C = 2*idx+1
                else : 
                    c = self.getLeftSubTree(a)
                    idx_C = 2*idx
                
                #전환
                if a<c:
                    self.items[idx], self.items[idx_C] = self.items[idx_C], self.items[idx]
                else : b = False

    def getLeftSubTree(self, item) :
        idx = self.items.index(item) 
        if len(self.items)-1 >= 2*idx :       #수정(함수 리턴값이 없는 예외경우를 만들지 않기 위해)
            return self.items[2*idx]
        else : return 0

    def getRightSubTree(self, item) :
        idx = self.items.index(item)
        if len(self.items)-1 >= 2*idx+1 :
            return self.items[2*idx+1]
        else : return 0

    def getParentNode(self,item) :
        idx = self.items.index(item)
        if len(self.items)-1 >= idx//2 :
            return self.items[idx//2]
        else : return 0

    def printHeap(self) :
        print('------------------------------')
        for _ in range(len(self.items)-1):    
            print(self.items[1])
            self.dele()
        print('------------------------------')

heap = Heap()
#adt 구현
while True:
    choose = int(input("연산 선택 : 추가(1), 삭제(2), 출력(3)"))
    if choose == 1:
        a = int(input(""))
        if a<=0:
            print("자연수를 적어주세요")
        else:    
            heap.setData(a)
    elif choose == 2:
        heap.dele()
    elif choose == 3:
        heap.printHeap()
        break