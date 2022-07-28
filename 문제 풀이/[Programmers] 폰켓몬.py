# level 1

def solution(nums):
    k = len(nums) // 2
    num_list = list(set(nums))
    if len(num_list) < k:
        k = len(num_list)
    return k

# 사실 두줄로 가능..

def solution(nums):
    return min(len(nums)/2, len(set(nums)))