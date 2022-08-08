def solution(N, road, K):
    answer = 0
    INF = K + 1
    graph = [[INF] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        graph[i][i] = 0

    for i in road:
        graph[i[0]][i[1]] = min(graph[i[0]][i[1]], i[2])
        graph[i[1]][i[0]] = min(graph[i[1]][i[0]], i[2])

    for _ in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                graph[a][b] = min(graph[a][_]+graph[_][b], graph[a][b])
                
    for i in graph[1]:
        if(i <= K):
            answer += 1

    return answer