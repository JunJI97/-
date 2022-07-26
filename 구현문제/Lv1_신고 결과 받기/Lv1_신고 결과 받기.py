def solution(id_list, report, k):
    answer = []
    dict_report = {}
    dict_count = {}
    ban_list = []

    for i in range(len(id_list)): 
        dict_report[id_list[i]] = []
        dict_count[id_list[i]] = 0

    for i in range(len(report)): # 집계
        id1, id2 = report[i].split()
        if(id2 in dict_report[id1]):
            pass
        else:
            dict_report[id1].append(id2)

    for key, val in dict_report.items():
        for i in range(len(val)):
            dict_count[val[i]] += 1

    for key, val in dict_count.items():
        if(val >= k):
            ban_list.append(key)

    for i in range(len(id_list)):
        temp_num = 0
        temp = dict_report[id_list[i]]
        for j in range(len(temp)):
            if(temp[j] in ban_list):
                temp_num += 1
        answer.append(temp_num)


    return answer