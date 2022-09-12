# level2 (dfs/bfs)
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# numbers 배열에 있는 숫자를 순서대로 더하거나 빼서 target으로 만들 수 있는 경우의 수

import queue

def solution(numbers, target):
    answer = 0
    q = queue.Queue()
    q.put((numbers[0], 0))
    q.put((-numbers[0], 0))
    while not q.empty():
        x, idx = q.get()
        idx += 1
        if idx < len(numbers):
            # idx를 왜 큐로 함께 가져가야 하는지?
            q.put((x + numbers[idx], idx))
            q.put((x - numbers[idx], idx))
        else:
            if x == target:
                answer += 1
            
    return answer

# 내가 작성한 답

import queue

def solution(numbers, target):
    answer = 0
    idx = 0
    q = queue.Queue()
    q.put(numbers[idx])
    q.put(-numbers[idx])
    while not q.empty():
        x = q.get()
        idx += 1
        if idx < len(numbers):
            q.put(x + numbers[idx])
            q.put(x - numbers[idx])
        else:
            if x == target:
                answer += 1
            
    return answer