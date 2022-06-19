import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 주어진 list를 heap으로 변환

    while(scoville[0] < K): # 가장 낮은 스코빌 지수가 K 이상이 될 때 까지 반복
        if(len(scoville) >= 2):
            first = heapq.heappop(scoville) # 가장 작은 스코빌 pop
            second = heapq.heappop(scoville) # 그 다음 작은 스코빌 pop
            mix = first + (second * 2) # 섞은 음식의 스코빌
            heapq.heappush(scoville, mix) # heap에 push
            answer += 1
        else:
            return -1


    return answer