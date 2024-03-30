graph = {'동수':['지민','지율'],
            '지민':['동수','민석'],
            '민석':['정희','수정','지민','지율'],
            '정희':['민석','수정'],
            '수정':['민석','정희'],
            '지율':['동수','민석'],
        }

#start : 시작 노드, visited : 방문 기록 저장 리스트
def DFS(graph, start, visited) :
    #스택 생성, 시작노드 스택에 추가
    stack = []
    stack.append(start)
    #스택이 비어있지 않다면 계속 반복
        #스택에서 pop한 데이터가 방문한적이 없다면,
        #방문했음을 기록하고
        #해당 데이터에 연결되어 있는 노드들을 차례로 스택에 추가
        #(단, 이미 방문한적이 있거나 이미 스택에 존재하는 경우 제외)
    while stack :
        node = stack.pop()
        if node not in visited :
            visited.append(node)
        for i in range(len(graph[node]), 0, -1):
            if graph[node][i-1] not in visited:
                stack.append(graph[node][i-1])




def selfDFS(graph, start, visited) :
    visited.append(start)
    for d in graph[start]:
        if d not in visited:
            selfDFS(graph,d,visited)


if __name__ == '__main__' :
    visited = []
    DFS(graph, '동수', visited)
    print(visited)
    visited.clear()
    selfDFS(graph, '동수', visited)
    print(visited)