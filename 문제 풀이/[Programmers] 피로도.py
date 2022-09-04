# level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    ans_list = []
    # permutations로 던전을 도는 순서의 모든 경우의 수 리스트 생성
    arr = list(permutations(dungeons, len(dungeons)))
    # 모든 경우의 수에 대해 ans_list에 수행 가능 횟수를 저장하고 max값 return
    for case in range(len(arr)):
        list_case = arr[case]
        count = 0
        caseK = k
        for dun in list_case:
            if caseK >= dun[0]:
                caseK -= dun[1]
                count += 1
        ans_list.append(count)
                
    answer += max(ans_list)
    return answer