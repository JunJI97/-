[문제링크](https://programmers.co.kr/learn/courses/30/lessons/43165)

# 문제 설명

n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

```
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.


**제한사항**
---------

 * 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
 * 각 숫자는 1 이상 50 이하인 자연수입니다.
 * 타겟 넘버는 1 이상 1000 이하인 자연수입니다.



**입출력 예**
-------------

numbers	| target	| return
---|---|---
[1, 1, 1, 1, 1]	| 3	| 5
[4, 1, 2, 1]	| 4	| 2


**입출력 예 설명**
--------------

입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

```
+4+1-2+1 = 4
+4-1+2-1 = 4
```
 * 총 2가지 방법이 있으므로, 2를 return 합니다.


# 풀이
```python
def solution(numbers, target):
    answer, prev, now = [], [0], []
    
    for i in range(len(numbers)): # 주어진 숫자 반복
        if(len(prev) != 1): 
            now = []
        for j in range(len(prev)): # 현재까지 저장된 계산결과 반복
            if(i == (len(numbers)-1)): # 마지막 라운드
                answer.append(prev[j] + numbers[i])
                answer.append(prev[j] - numbers[i])
            else:
                now.append(prev[j] + numbers[i])
                now.append(prev[j] - numbers[i])
        prev = now
                    
    return answer.count(target)
```
간단한 수준의 탐색문제 


**다른 사람의 풀이와 효율성 비교**
--------------
 다른 사람의 풀이도 기본적으로 똑같은 매커니즘이였으나, 재귀함수 또는 map을 활용하여 코드를 훨씬 짧게 구현하였다.
 특히, map을 활용한 풀이는 나의 통과시간보다 좀 더 빠른 속도를 보였다.
 
 ![image](https://user-images.githubusercontent.com/102650903/175257850-3dde0f22-a2f5-44ba-9932-52bccc092900.png)
<내가 푼 방법의 속도>

![image](https://user-images.githubusercontent.com/102650903/175257934-16baff08-3e6b-4aff-b559-c789bc04c7d7.png)
<다른사람의 풀이 중 가장 빨랐던 문제의 속도 (map 활용)>




