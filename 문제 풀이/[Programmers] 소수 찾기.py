# level 2
# numbers = "17", "011"...
# 주어진 문자열을 조합하여 만들 수 있는 수 중 소수의 개수 return

from itertools import permutations

def solution(numbers):
    count = 0
    # 문자열을 슬라이싱하여 리스트화
    num_list = [i for i in numbers]
    dp = []
    # 모든 조합 리스트 생성
    for j in range(1, len(num_list)+1):
        dp += list(permutations(num_list, j))
    # 숫자로 변환
    dpL = [int("".join(l)) for l in dp]
    # 중복 제거
    dpM = list(set(dpL))
    # 소수 판별
    for k in dpM:
        if k >= 2:
            check = True
            for n in range(2, k):
                if k % n == 0:
                    check = False
                    break
            if check:
                count += 1
    return count