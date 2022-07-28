[문제링크](https://school.programmers.co.kr/learn/courses/30/lessons/12926)

# 문제 설명

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

**제한사항**
---------

 * 공백은 아무리 밀어도 공백입니다.
 * s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
 * s의 길이는 8000이하입니다.
 * n은 1 이상, 25이하인 자연수입니다.



**입출력 예**
-------------

s	| n	| result
---|---|---
"AB"	| 1	| "BC"
"z"	| 1	| "a"
"a B z"	| 4	| "e F d"


# 풀이
```python
def solution(s, n):
    answer = ''
    big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for i in range(len(s)):
        if(s[i] in big):
            index = big.index(str(s[i]))
            if(index + n) >= 26:
                answer += str(big[index + n - 26])
            else:
                answer += str(big[index + n])
        elif(s[i] in small):
            index = small.index(str(s[i]))
            if(index + n) >= 26:
                answer += str(small[index + n - 26])
            else:
                answer += str(small[index + n])
        else:
            answer += " "
    return answer
```
그냥 손풀기용 문제, 배열의 인덱스를 이용해 구현

만약 C언어로 구현했다면, 아스키코드로 변환해 풀었겠지만 파이썬에선 방법을 몰랐어서 배열을 이용했다.


**다른 사람의 풀이**
--------------

ord() 함수 : 문자 하나를 아스키 코드로 변환
chr() 함수 : 아스키코드를 문자로 변환

ord,chr 함수를 이용한 방법으로 훨씬 짧고 가독성있게 구현할 수 있다.



