def printSolution(map, numOfQueens) :
    for i in range(numOfQueens) :
        for j in range(numOfQueens) :
            if map[i] == j :
                print('Q',end='')
            else :
                print('.',end='')
        print()
    print()


def isThreatened(map, newRow) :
    curRow = 0
    flag = False
    
    while curRow < newRow :
        if map[newRow] == map[curRow] or \
            abs( map[newRow] - map[curRow] ) == abs( newRow - curRow ) :
            flag = True
            break
        
        curRow += 1

    return flag


# map : 부분해 담고 있는 공간
# row : 새 퀸이 놓인 행 번호
# numOfQueens : 체스판의 크기
# solutionCount : 해가 몇개인가
def findSolutionForQueen(map, row, numOfQueens) :
    global solutionCount
    # 새로 놓은 퀸이 기존의 퀸들에게 위협받는지 알아내기
    # 위협한다면 함수를 반환하여 "백트래킹" !!
    if isThreatened(map, row) :
        return
    
    if row == numOfQueens -1 :
        solutionCount += 1
        print('[ solution {} ]'.format(solutionCount))
        printSolution(map, numOfQueens)
    else :
        for i in range(numOfQueens) :
            map[row+1] = i
            findSolutionForQueen(map, row+1, numOfQueens)
            
#-------------------------------------------------------------------------
            
num = int(input('퀸 개수 : '))
map = [0] * num
solutionCount = 0

for i in range(num) :
    map[0] = i
    findSolutionForQueen(map, 0, num)