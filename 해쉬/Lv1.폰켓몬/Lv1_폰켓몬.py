def solution(nums):
    answer = 0
    dest = int(len(nums) / 2)
    arr = []
    for i in range(len(nums)):
        if nums[i] in arr:
            pass
        else:
            arr.append(nums[i])
            
    if len(arr) >= dest:
        return dest
    else:
        return len(arr)