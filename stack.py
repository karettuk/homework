class Stack:
    def __init__(self, c=10):
        self.items = [None]*c
        self.capacity = c
        self.top = 0
    def push(self,item):
        if self.capacity > self.top:
            self.items[self.top] = item
            self.top +=1
        else : print("Stack is full.")
    def pop(self):
        if self.top == 0:
            print("스택에 삭제할 데이터가 없습니다.")
            return
        else : 
            data = self.items[self.top-1]
            self.items[self.top-1] = None
            self.top -= 1
            return data
    def peek(self):
        if self.top == 0:
            print("스택에 꺼낼 데이터가 없습니다.")
            return
        else: return self.items[self.top-1]
    def printStack(self):
        print('------------')
        for i in range(self.top, 0, -1):
            print(self.items[i-1])
        print('------------')
    def is_empty(self):
        if self.top == 0:
            return True
        else: return False
def getPriority(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    else : return -1
def getPostfix(infix):
    postfix = ''
    stack=Stack()
    pos=0
    op=['+','-','*','/']
    while infix != None and pos < len(infix):
        ch = infix[pos]
        if ch in op: #연산자 인식
            while stack.is_empty() != True and getPriority(ch) <= getPriority(stack.peek()):
                postfix += stack.pop()
            stack.push(ch)
        elif ch == '(': #여는 괄호 인식
            stack.push(ch)
        elif ch == ')': #닫는 괄호 인식
            while True:
                data = stack.pop()
                if data == '(':
                    break
                postfix += data
        else:postfix+=ch #나머지 숫자 인식
        pos += 1
    while stack.is_empty() != True: #스택 처리 후 스택에 남은 나머지 연산자 꺼내서 처리
        postfix += stack.pop()
    return postfix
def calculator(postfix):
    stack = Stack(10)
    op=['+','-','*','/']
    pos = 0
    result = 0
    while postfix != None and pos < len(postfix):
        ch = postfix[pos]
        if ch not in op:
            ch = int(ch)
            stack.push(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if ch == '+':result = op1+op2
            elif ch == '-':result = op2-op1
            elif ch == '*':result = op1*op2
            elif ch == '/':result = op2/op1  #op2를 썼어야 했는데 op만 썼음!
            stack.push(result)
        pos += 1
    return stack.pop()
if __name__ == '__main__':
    infix = ''
    postfix = ''
    while True:
        print("1,수식 입력")
        print("2, 후위수식으로 변경")
        print("3,계산")
        print("4, 종료")
        menu = int(input("선택 => "))
        if menu==1:
            infix = "(5-2)/3"
            print('infix : '+infix)
        elif menu == 2:
            postfix = getPostfix(infix)
            print('postfix : '+postfix)
        elif menu == 3:
            print(infix, '=', calculator(postfix))
        elif menu == 4:
            print("프로그램 종료!")
            break
        else : print("메뉴에 없는 번호를 입력했습니다.다시 입력해주세요.")