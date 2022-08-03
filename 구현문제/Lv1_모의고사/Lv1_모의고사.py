def solution(answers):  
    p1 = [1,2,3,4,5] #5
    p2 = [2,1,2,3,2,4,2,5] #8
    p3 = [3,3,1,1,2,2,4,4,5,5] #10        
    answer = []
    
    count1, count2, count3 = 0,0,0
    
    for i in range(len(answers)):
        temp = int(answers[i])
        if temp == p1[i%5]:
            count1 +=1
        if temp == p2[i%8]:
            count2 +=1
        if temp == p3[i%10]:
            count3 +=1
    arr = [count1,count2,count3]
    most_score = max(arr)
    for i in range(3):
        if(most_score == arr[i]):
            answer.append(i+1)
    return answer