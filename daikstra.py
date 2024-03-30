# 개선점 : 입력 원활하게(A,C,10 -> A로부터 C까지의 간선이 있고 그 간선의 가중치는 10이다.)
# 노드 이름 만들 수 있게(A노드 : 세상에 이런 건 없으 -> ##백화점 : 뭔가 현실적이야~)
#어떤 노드에서 시작하든 상관없게(굳이 1번 노드부터 해야 제대로 작동하니 매우 불편)

def daikstra(graph, node):
    #초기화
    distance = []
    visited = []
    not_visited = []
    for i in range(node):
        if i == 0: distance.append(0)
        else : distance.append(2147483647)
        not_visited.append(i)

    #다익스트라
    for i in range(len(graph)):
        nvdistance = []
        for b in not_visited:
            nvdistance.append(distance[b])
        for c in range(len(distance)):
            if min(nvdistance) == distance[c]:
                if c in not_visited:
                    a = c
        visited.append(a)
        not_visited.remove(a)
        for h in graph[a]:
            if h != 0:
                if distance[graph[a].index(h)] == 2147483647:
                    distance[graph[a].index(h)] = 0
                    distance[graph[a].index(h)] = distance[a]+h
                else : 
                    if distance[a] + h < distance[graph[a].index(h)]:
                        distance[graph[a].index(h)] = distance[a] + h
    return distance

"""if __name__ == '__main__':
    node = int(input("몇 개의 노드를 가지고 다익스트라 알고리즘을 실행할까요?"))
    graph = []
    print("어떻게 그래프를 구성할 지 1번 노드부터 인접행렬 방식으로 작성해주세요")
    for _ in range(node):
        mapping = list(map(int, input().split()))
        graph.append(mapping)
    print(graph)
    destination = int(input(("몇 번 노드까지의 최소 거리를 구하고 싶으신가요?")))
    print(daikstra(graph, node)[destination-1])"""


if __name__ == '__main__':
    node = int(input("몇 개의 장소가 있나요?"))
    place = list(map(str, input("각각의 장소 이름은 무엇인가요?").split()))
    graph = []
    for _ in range(node):
        graph.append([0]*node)
    for _ in range(node):
        mapping = list(map(str, input("어떻게 그래프를 구성할 지 작성해주세요").split()))
        graph.append(mapping)
    print(graph)
    destination = int(input(("몇 번 노드까지의 최소 거리를 구하고 싶으신가요?")))
    print(daikstra(graph, node)[destination-1])