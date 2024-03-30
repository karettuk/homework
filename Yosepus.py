class Queue :
    def __init__(self) :
        self.items = []

    def enqueue(self, item) :
        self.items.append(item)

    def dequeue(self) :
        if len(self.items) != 0 :
            return self.items.pop(0)
        else :
            print('Queue is empty.')
            
    def peek(self) :
        size = len(self.items)
        if size != 0 :
            return self.items[0]
        else :
            print('Queue is empty')
    
    def printQueue(self) :
        for i in self.items :
            print(i, end='  ')
        print()

    def circle(self, num):
        for _ in range(1,num):
            last = self.dequeue()
            self.enqueue(last)
a = int(input(""))
b= int(input(""))
origin = Queue()
numlist = []
for i in range(1,a+1):
    origin.enqueue(i)
for i in range(1,a+1):
    origin.circle(b)
    num = origin.dequeue()
    numlist.append(num)
print(numlist)