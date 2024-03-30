import queue
n, m = map(int, input().split())
maze = []
for _ in range(n):
    ma = list(map(int,input().split()))
    maze.append(ma)
#2차원 공간에서 x,y좌표의 변화
dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = queue.Queue()
q.put([0,0])
while not q.empty():
    x,y = q.get()
    print("현재 위치 {},{}".format(x,y))
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n :continue
        if ny<0 or ny>=m : continue
        if maze[nx][ny] == 0 : continue
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            q.put([nx,ny])
print(maze)
print("최단 거리 : {}".format(maze[n-1][m-1]))
