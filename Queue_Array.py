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

if __name__ == '__main__' :
    queue = Queue()
    queue.enqueue('c:')
    queue.enqueue('cf')
    queue.enqueue('c1f')
    queue.enqueue('c2.pptx')
    queue.printQueue()
    queue.dequeue()
    print(queue.peek())
    queue.dequeue()
    queue.printQueue()