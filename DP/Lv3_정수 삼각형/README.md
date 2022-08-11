[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/43105)

# 문제 설명

![image](https://user-images.githubusercontent.com/102650903/184241135-080b04da-180d-41d7-acbe-4f8661f1075f.png)

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.


**제한사항**
---------

 * 삼각형의 높이는 1 이상 500 이하입니다.
 * 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.


**입출력 예**
-------------

triangle	| result
---|---
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	| 30


# 풀이
```python
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
```

같은 동적계획법 문제인 <N으로 표현>이랑 같은 3레벨 문제이지만, 난이도 측정이 잘못된 것 같다.
3레벨 치곤 너무 쉬웠던 문제.


