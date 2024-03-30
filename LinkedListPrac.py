class Student:
    def __init__(self, na, nu, gr):
        self.name = na
        self.num = nu
        self.grade = gr
    def __str__(self):
        return("[{}({}) : {}]".format(self.name, self.num, self.grade))
class Node:
    def __init__(self, d, nx):
        self.data = d
        self.next = nx
    def __str__(self):
        return(self.data)
class LinkedList : 
    def __init__(self):
        self.no = 0
        self.head = None
    def __len__(self):
        return(self.no)
    def addLast(self, d):
        if self.head == None : 
            self.head = Node(d,None)
            self.no += 1
        else : 
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(d,None)
            self.no += 1
    def remove(self, p) :
        if self.head != None :
            if self.head.data ==  p:
                self.head = self.head.next
            else :
                ptr = self.head
                while ptr.next.data != p :
                    ptr = ptr.next
                    if ptr == None :
                        return
                ptr.next = ptr.next.next
            self.no -= 1
    def insert(self, i, d):
        if i==0:
            self.head = Node(d,self.head)
        else :
            ptr = self.head
            for c in range(0, i-1):
                ptr = ptr.next
            ptr.next = Node(d,ptr.next)
        self.no += 1
    def print(self): 
        pres = self.head
        for i in range(1,self.no+1):
            if i == self.no:
                print(pres.data)
            else:
                print(pres.data, end=" -> ")
                pres = pres.next
        
arr = LinkedList()
s1 = Student(312, "김윤성", 4.3)
s2 = Student(315, "최누리", 4.1)
s3 = Student(317, "이기훈", 4.5)
arr.addLast(s1)
arr.insert(0,s2)
arr.insert(1,s3)
print(len(arr))
arr.print()