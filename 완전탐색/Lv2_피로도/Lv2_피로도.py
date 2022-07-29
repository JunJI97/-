from itertools import permutations
def solution(k, dungeons):
    answer = []
    C = list(permutations(dungeons,len(dungeons))) # 순열

    for i in C:
        state = k
        count = 0
        for j in i:
            if(state >= j[0]):
                count += 1
                state -= j[1]
            else:
                continue
        answer.append(count)

    return max(answer)