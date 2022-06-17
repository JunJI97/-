[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42842)

# 문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

![image](https://user-images.githubusercontent.com/102650903/174382317-49d447a0-f140-4c47-b347-f7171b52632d.png)

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.


**제한사항**
---------

* 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
* 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
* 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.



**입출력 예**
-------------
brown |	yellow	| return
---|---|---
10	| 2	|	[4, 3]
8	|	1	|	[3, 3]
24	|	24	|	[8, 6]



# 풀이
```python
def solution(brown, yellow):
    for line in range(1, yellow+1): # yellow의 line 수
        w = yellow / line # yello 가로 길이
        if(w - int(w)) == 0.0: # yellow 타일이 여러 라인을 가질 수 있는 경우
            w = int(w)
            pre_brown = (w + 2)*2 + (line * 2) # 예상 brown 타일 수 계산
            if (pre_brown == brown): # 예상한 bronw 타일 수가 주어진 값과 일치할 때
                return [w+2, line+2]
        else:
            pass
    return -1
```



 
 


