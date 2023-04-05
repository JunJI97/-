import sys

def sol():
    sys.stdin = open("1.txt", "r")
    map_size, remain_num = map(int,input().split())
    store_list = []
    house_list = []
    graph = []

    for i in range(map_size):
        row = list(map(int,input().split()))
        graph.append(row)

    for h in range(0,map_size):
        for w in range(0,map_size):
            if graph[h][w] == 2:
                store_list.append([h,w])
            if graph[h][w] == 1:
                house_list.append([h,w])

    picked_store = get_comb(store_list, remain_num)
    answer = []
    for arr in picked_store:
        temp1 = [] # 집 마다 최적의 치킨 거리 모음
        for a in house_list: # 일반집
            temp2 = []  # 해당 집에서 갈 수 있는 치킨 가게의 거리 모음
            for b in arr: # 치킨집
                temp2.append(cal_dist(a,b))
            temp1.append(min(temp2))
        answer.append(sum(temp1))

    return min(answer)



def get_comb(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        item = arr[i]
        temp = arr[i+1:]
        for c in get_comb(temp, n-1):
            result.append([item] + c)
    return result

def cal_dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sol()