#서로소 집합 알고리즘!!(문제에서 많이 사용됨)
def find_parent(plist, x) :
    #루트 노드가 아니라면 루트노드를 찾을 때까지 재귀 호출
    if plist[x] != x :
        plist[x] = find_parent(plist, plist[x])
        
    return plist[x]


def union_node(plist, a, b) :
    a = find_parent(plist, a)
    b = find_parent(plist, b)
    if a < b :
        plist[b] = a
    else :
        plist[a] = b
        
#----------------------------------------------------------------
#정점 저장
plist = []
home, street = map(int, input("집 개수, 도로 개수 : ").split())
for i in range(home):
    plist.append(i)

#그래프에서 간선을 저장
edges = []
origincost = 0
for i in range(street) :
    start, end, cost = map(int, input().split())
    edges.append((cost,start,end))
    origincost += cost
edges.sort() #sort에서 튜플은 맨 앞 속성을 기준으로 정렬됨

realcost = 0
edgeNums = 0
while(edgeNums < home-1):
    cost, a, b = edges.pop(0)
    #간선의 양 끝 노드가 속한 집합 구하기!!
    ap = find_parent(plist,a)
    bp = find_parent(plist,b)
    if ap != bp:
        #print('간선 추가 : {}, {}, {}'.format(a,b,cost))
        union_node(plist, ap, bp)
        realcost += cost
        edgeNums += 1
print(origincost - realcost)