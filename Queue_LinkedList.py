class Node :
    def __init__(self,value,link) :
        self.value = value
        self.next = None


class Queue :
    def __init__(self) :
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item) :
        node = Node(item, None)
        if not self.front :
            self.front = node
            self.rear = node
        else :
            if self.rear :
                self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self) :
        if self.size != 0 :
            node = self.front
            self.front = self.front.next
            self.size -= 1
            return node.value
        else :
            print('Queue is empty.')


    def printQueue(self) :
        node = self.front
        while node :
            print(node.value, end=' ')
            node = node.next
        print()

    
if __name__ == '__main__' :
    queue = Queue()
    queue.enqueue('c:')
    queue.enqueue('cf')
    queue.enqueue('c1f')
    queue.enqueue('c2.pptx')
    queue.printQueue()
    queue.dequeue()
    queue.dequeue()
    queue.printQueue()
    