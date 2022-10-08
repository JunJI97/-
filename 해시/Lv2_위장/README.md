[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

# 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.



**제한사항**
---------

 * genres[i]는 고유번호가 i인 노래의 장르입니다.
 * plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
 * genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
 * 장르 종류는 100개 미만입니다.
 * 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
 * 모든 장르는 재생된 횟수가 다릅니다.



**입출력 예**
-------------

genres	| plays	| return
---|---|---
["classic", "pop", "classic", "classic", "pop"]	| [500, 600, 150, 800, 2500]	| [4, 1, 3, 0]




**입출력 예 설명**
--------------

classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

 * 고유 번호 3: 800회 재생
 * 고유 번호 0: 500회 재생
 * 고유 번호 2: 150회 재생
 
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

 * 고유 번호 4: 2,500회 재생
 * 고유 번호 1: 600회 재생
 
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

 * 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.
 

# 풀이
```python
def solution(genres, plays):
    answer = []
    arr = []
    dict_music = {}
    total = {}

    # dict_music에 장르 별 정리
    for i in range(len(genres)):
        if(genres[i] not in dict_music): 
            dict_music[genres[i]] = []
            total[genres[i]] = 0
        
        dict_music[genres[i]].append([plays[i],i])
        total[genres[i]] += plays[i]

    # 각각 장르의 [총 재생 횟수, 장르] 데이터를 arr 배열에 추가해 재생 수가 많은 숫자가 앞에오도록 내림차순 
    for k, v in total.items():
        arr.append([v,k])
    arr.sort(reverse = True)
        
    # arr에서 정리된 장르 순서대로 dict_music 참조 (재생순서 내림차순 같은 경우는 고유번호가 빠른 순서로)
    for i in range(len(arr)):
        f = sorted(dict_music[arr[i][1]], key = lambda x : (-x[0], x[1]))
        if len(f) == 1: # 해당 장르의 곡이 하나인 경우
            answer.append(f[0][1])
        else: # 해당 장르에서 재생이 많이된 두 곡 저장
            answer.append(f[0][1])
            answer.append(f[1][1])

    return answer
```
        
![image](https://user-images.githubusercontent.com/102650903/191268322-65042f85-864f-4a3c-ba20-5abaff68584c.png)
테스트 케이스

![image](https://user-images.githubusercontent.com/102650903/191268397-d4f3a844-1e1f-44cd-afeb-3d2b96b2c624.png)

print(dict_music) 결과

![image](https://user-images.githubusercontent.com/102650903/191268515-f2de85b1-b369-41e3-998e-c4f12c2c2340.png)

print(arr) 결과

** 다중 기준으로 정렬하는 법**
-------------

예시 ) 첫번째 요소 기준으로 내림차순, 같을 시 두번째 기준으로 
sorted_list = sorted(정렬할 리스트, key = lambda x : (-x[0], x[1]))
