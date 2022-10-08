def solution(n, computers):           
    
    answer = 0
    visited = [] # 방문기록
    temp = [] # 임시 배열
     
    def bfs(index): 
        if index in visited:
            pass
        else:
            visited.append(index)
            temp.append(index)
            for k in range(n):
                if(computers[index][k] == 1) and (k not in visited):
                    bfs(k) # 재귀
    
    for i in range(n):
        if i in visited:
            pass
        else:
            bfs(i)
            answer += 1
            temp.clear()
    return answer