def solution(brown, yellow):
    for line in range(1, yellow+1): # yellow의 line 수
        w = yellow / line # yello 가로 길이
        if(w - int(w)) == 0.0: # yellow 타일이 여러 라인을 가질 수 있는 경우
            w = int(w)
            pre_brown = (w + 2)*2 + (line * 2) # 예상 brown 타일 수 계산
            if (pre_brown == brown): # 예상한 bronw 타일 수가 주어진 값과 일치할 때
                return [w+2, line+2]
        else:
            pass
    return -1