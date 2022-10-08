[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42578)

# 문제 설명

스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

종류 |이름
---|---|
얼굴 | 동그란 안경, 검정 선글라스
상의 |	파란색 티셔츠
하의 |	청바지
겉옷 | 긴 코트

스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.



**제한사항**
---------

* clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
* 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
* 같은 이름을 가진 의상은 존재하지 않습니다.
* clothes의 모든 원소는 문자열로 이루어져 있습니다.
* 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
* 스파이는 하루에 최소 한 개의 의상은 입습니다.



**입출력 예**
-------------
clothes	| return
---|---
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	| 5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]] | 3




**입출력 예 설명**
--------------

예제 #1

headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

    1. yellow_hat
    2. blue_sunglasses
    3. green_turban
    4. yellow_hat + blue_sunglasses
    5. green_turban + blue_sunglasses 

예제 #2

face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

    1. crow_mask
    2. blue_sunglasses
    3. smoky_makeup


# 풀이
```python
def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    # dict으로 정리
    for i in range(len(clothes)):
        key = clothes[i][1] # 옷의 분류
        value = clothes[i][0] # 명칭
        if(key in clothes_dict): 
            clothes_dict[key] += 1
        else:
            clothes_dict[key] = 1
    
    print(clothes_dict)
    
    # (종류1 개수 + 1) * (종류2 개수 + 1) * .... -1 = 답
    for key, value in clothes_dict.items():
        answer *= (value+1)
    
    return answer-1
```
        
 dict 형태로 입력값을 정리하고 경우의 수를 최종적으로 계산하면 되는 간단한 문제

**dict으로 정리한 결과**
![image](https://user-images.githubusercontent.com/102650903/173249799-ca1b1bee-7297-4752-aadf-5ec90b2d34a4.png)

**계산식**

(종류1 개수 + 1) * (종류2 개수 + 1) * .... -1 = 답

1. 1을 더하고 곱하는 이유 : 해당 부위의 옷을 착용안하는 경우도 있기때문
2. 마지막에 1 빼는 이유 : 옷을 전혀 입지 않은 경우를 배제함

**새로 배운 내용**
------------------------

for key, value in clothes_dict.items():

.items()를 사용하여 딕셔너리에 있는 key,value값 모두 접근가능!

 
 


