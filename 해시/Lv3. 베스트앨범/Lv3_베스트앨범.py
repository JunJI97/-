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