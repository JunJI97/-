from collections import deque

def solution(progresses, speeds):
    answer = []
    sch = deque() # 필요 작업일자 담은 큐 생성
    for i in range(len(progresses)):
        dday = (100 - progresses[i]) / speeds[i] # 필요한 day
        if(dday % 1 == 0.0):
            sch.append(int(dday))
        else:
            sch.append(int(dday+1))
    
    while(len(sch) != 0): # 큐 모두 소모까지 반복
        count = 0 # 다음 배포까지 작업완료되는 작업 수 
        temp = sch[0] # 현재 가장 높은 우선순위 작업의 남은 작업일자
        for i in range(len(sch)): 
            if temp >= sch[i]:
                count += 1
            else:
                break
        answer.append(count)
        for i in range(count):
            sch.popleft()
                
    return answer