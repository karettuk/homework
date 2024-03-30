graph = {'동수':['지민','지율'],
            '지민':['동수','민석'],
            '민석':['정희','수정','지민','지율'],
            '정희':['민석','명석','수정'],
            '수정':['민석','정희'],
            '지율':['동수','민석'],
            '명석':['정희']
        }

def BFS(graph, start, visited) :
    #큐 생성해서 시작 노드 추가
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visited: 
            visited.append(node)
            for i in range(len(graph[node])):
                if graph[node][i] not in visited and graph[node][i] not in queue:
                    queue.append(graph[node][i])
    #큐가 비어있지 않다면 계속 반복
        #큐에서 pop한 데이터가 방문한적이 없다면,
        #방문했음을 기록하고
        #해당 데이터에 연결되어 있는 노드들을 차례로 큐에 추가
        #(단, 이미 방문한적이 있거나 이미 큐에 존재하는 경우 제외)
    pass



if __name__ == '__main__' :
    visited = []
    BFS(graph, '지율', visited)
    print(visited)