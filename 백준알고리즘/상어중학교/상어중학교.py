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
        # if big_group == []:
        #     return answer
        # graph에서 big_group 삭제
        # big_group 사이즈 제곱만큼 점수 계산
        # gravity_graph()
        # rotate_90()
        # gravity_graph()

    return 0

def search_group(graph, M):
    group = []
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
        # print(" --> 그룹은 {}".format(made_group))
        return made_group

    for h in range(M):
        for w in range(M):
            node = [h,w]
            value = graph[h][w]
            if value > 0:
                q = deque([[h, w]])
                # print("======== {} {} 에서 탐색 시작".format(h,w))
                temp_group = dfs(q, value)
                if group == [] or len(group) < len(temp_group):
                    group = temp_group
    print(" --> 가장 큰 그룹은 {}".format(group))
    return group

def rotate_90():
    return 0

def gravity_graph():
    return 0


sol()
