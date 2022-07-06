def solution(citations):
    answer = 0
    sorted_citations = sorted(citations, reverse = True)
    
    for i in range(len(sorted_citations)):
        h = sorted_citations[i]
        answer += 1
        if(h >= answer):
            pass
        else: 
            return answer-1
        
    return answer