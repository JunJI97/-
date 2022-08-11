def solution(triangle):
    if(len(triangle) == 1):
        return triangle[0][0]
    answer = triangle[0]
    for i in range(1,len(triangle)): # 꼭대기에서 바닥으로 순회
        temp = [] # 임시 배열 생성
        n = len(triangle[i])
        for j in range(n): # 해당 층까지 누적된 값 중 큰 것만 빈 배열에 추가
            if(j == 0):
                temp.append(triangle[i][j] + answer[0])
            elif(j == (n-1)):
                temp.append(triangle[i][j] + answer[-1])
            else:
                temp.append(max(triangle[i][j] + answer[j-1],triangle[i][j] + answer[j]))
        answer = temp # 채워진 배열을 answer로 바꾸고 해당 값들로 다시 순회
                
    return max(answer)