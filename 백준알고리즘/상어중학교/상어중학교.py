import sys
from collections import deque
def sol():
    sys.stdin = open("1.txt", "r")
    M, N = map(int,input().split())

    answer = 0
    graph = []
    for i in range(M):
        row = list(map(int,input().split()))
        graph.append(row)

    while(1):
        big_group = search_group(graph, M)
        score = len(big_group)
        if big_group == []:
            print(answer)
            return answer
        delete_group(graph, big_group)
        answer += (score*score)
        for r in range(M):
            gravity_graph(graph,M)
        graph = rotate_90(graph, M)
        for r in range(M):
            gravity_graph(graph,M)

    return answer

def search_group(graph, M):
    group = []
    visited = []
    # 복 동 남 서
    dh = [-1,0,1,0]
    dw = [0,1,0,-1]

    def dfs(q, value):
        made_group = []
        visited = []
        while q:
            item = q.popleft()
            h,w = item[0], item[1]

            if len(made_group) == 0:
                made_group.append([h, w])
                visited.append([h,w])

            for d in range(4): # 인접 4블럭 확인
                nh = h + dh[d]
                nw = w + dw[d]
                if [nh, nw] not in visited and 0 <= nh < M and 0 <= nw < M: # 범위 내, 방문 경험 없는 노드
                    if graph[nh][nw] in [value, 0]:
                        q.append([nh,nw])
                        made_group.append([nh,nw])
                        visited.append([nh,nw])

        return made_group

    for h in range(M):
        for w in range(M):
            value = graph[h][w]
            if value > 0:
                q = deque([[h, w]])
                if [h,w] not in visited:
                    temp_group = dfs(q, value)
                else:
                    temp_group = []
                for k in temp_group:
                    if graph[k[0]][k[1]] != 0:
                        visited.append(k)
                if len(temp_group) > 1:
                    if group == [] or len(group) < len(temp_group): # 그룹블록 우선순위 결정
                        group = temp_group
                    elif len(group) == len(temp_group):
                        group = pick_big_group(graph, group,temp_group)

    return group

def delete_group(graph, big_group):
    for delete in big_group:
        graph[delete[0]][delete[1]] = -2
    return graph


def gravity_graph(graph,M):
    for w in range(M):
        for h in range(M):
            item = graph[h][w]
            if item >= 0: # 드랍 대상
                if h+1 < M and graph[h+1][w] == -2:
                    graph[h][w] = -2
                    graph[h+1][w] = item

    return graph

def rotate_90(graph,M):

    rotated_graph = [[0]*M for _ in range(M)]
    for h in range(M):
        for w in range(M):
            rotated_graph[M-1-w][h] = graph[h][w]
    return rotated_graph

def pick_big_group(graph ,group1,group2):
    count1 = 0
    count2 = 0
    standard1 = []
    standard2 = []

    for i in group1:
        if graph[i[0]][i[1]] == 0:
            count1 += 1
        else:
            standard1.append(i)

    for i in group2:
        if graph[i[0]][i[1]] == 0:
            count2 += 1
        else:
            standard2.append(i)

    # 우선 순위 1 : 0을 더 많이 소유한 그룹
    if count1 > count2:
        return group1
    elif count1 < count2:
        return  group2
    else: # 우선 순위 2 : 기준 블록의 행이 가장 큰 것
        standard1.sort()
        standard2.sort()
        if standard1[0][0] > standard2[0][0]:
            return group1
        elif standard1[0][0] < standard2[0][0]:
            return  group2
        else: # 우선 순위 2 : 기준 블록의 열이 가장 큰 것
            if standard1[0][1] > standard2[0][1]:
                return group1
            elif standard1[0][1] < standard2[0][1]:
                return group2

    return group1


sol()
