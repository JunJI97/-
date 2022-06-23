def solution(numbers, target):
    answer, prev, now = [], [0], []
    
    for i in range(len(numbers)): # 주어진 숫자 반복
        if(len(prev) != 1): 
            now = []
        for j in range(0,2): # +,-
            for k in range(len(prev)): # 현재까지 저장된 계산결과 반복
                if(j == 0): # plus
                    if(i == (len(numbers)-1)): # 마지막 라운드
                        answer.append(prev[k] + numbers[i])
                    else:
                        now.append(prev[k] + numbers[i])
                else: # minus
                    if(i == (len(numbers)-1)): # 마지막 라운드
                        answer.append(prev[k] - numbers[i])
                    else:
                        now.append(prev[k] - numbers[i])
        prev = now
                    
    return answer.count(target)