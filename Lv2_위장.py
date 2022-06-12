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
    
    # (종류1 개수 + 1) * (종류1 개수 + 1) * .... -1 = 답
    for key, value in clothes_dict.items():
        answer *= (value+1)
    
    return answer-1