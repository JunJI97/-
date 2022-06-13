def solution(phone_book):
    phone_book.sort() # 정렬
    for i in range(len(phone_book)-1): # -1 하는 이유는 아래 조건문 때문 (범위 이탈 방지)
        if(phone_book[i] == phone_book[i+1][0:len(phone_book[i])]): # 정렬 후 바로 옆 문자열끼리만 비교 하면 됨
            return False
    return True