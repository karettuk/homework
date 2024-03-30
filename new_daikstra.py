def choose_vertex(dist, found) :
    min = INF
    minpos = -1
    for i in range(len(dist)) :
        if dist[i] < min and found[i] == False :
            min = dist[i]
            minpos = i
    
    return minpos


def shortest_path_dijkstra(vertex, matrix, start) :
    vsize = len(vertex)
    dist = list(matrix[start])    
    found = [False] * vsize
    path = [start] * vsize 
    
    found[start] = True # 시작정점 이미 찾은 경우이므로 True
    dist[start] = 0 #시작정점과의 거리는 무조건 0
    
    for i in range(vsize) :
        #각 단계별 출력용 코드
        print("{}단계 : {}".format(i+1, dist))
        
        #현재 가장 낮은 경로인 정점을 최단경로에 포함시키기
        pick = choose_vertex(dist, found)
        found[pick] = True
        
        #현재 포함된 최단경로와의 거리 갱신
        for i in range(vsize) :
            if not found[i]  : #아직 최단 경로로 확정되지 않은 정점들만 갱신
                if dist[i] > dist[pick] + matrix[pick][i] :
                    dist[i] = dist[pick] + matrix[pick][i]
                    path[i] = pick                    
    return dist


#-------------------------------------------------------------------------------

vertex = ['A','B','C','D','E','F','G']
INF = 999 #무한대
matrix =[
    [0,     7,      INF,    INF,    3,      10,     INF],
    [7,     0,      4,      10,     2,      6,      INF],
    [INF,   4,      0,      2,      INF,    INF,    INF],
    [INF,   10,     2,      0,      11,     9,      4],
    [3,     2,      INF,    11,     0,      INF,    5],
    [10,    6,      INF,    9,      INF,    0,      INF],
    [INF,   INF,    INF,    4,      5,      INF,    0]
]

path = shortest_path_dijkstra(vertex, matrix, 0)

print(path)