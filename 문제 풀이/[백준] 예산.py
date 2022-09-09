# 2512번(이진탐색)
# 총 예산과 각 지방 단체 별로 요구하는 예산이 주어짐
# 총 예산을 가장 많이 분배할 수 있는 상한액 ans를 return 
# budget = 485, arr = [120, 110, 140, 150]

# 상한액이 주어졌을 때, 분배합 구하는 함수
def bud_cal(num, arr):
    bud = 0
    for i in arr:
        bud += min(i, num)
    return bud

# 이진 탐색으로 탐색 범위를 좁혀가며 탐색        
def solution(budget, arr):
    answer = []
    low = 0
    high = max(arr)
    while low < high:
        mid = (low + high) // 2
        if bud_cal(mid, arr) <= budget:
            answer.append(mid)
            low = mid+1
        if bud_cal(mid, arr) > budget:
            high = mid-1
    return max(answer)