def solution(a, b):
    day = 0
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    for i in range(a-1):
        day += mon[i]
    day += b

    return week[day % 7 -1]