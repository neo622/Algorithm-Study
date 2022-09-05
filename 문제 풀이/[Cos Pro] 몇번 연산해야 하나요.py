# 사용 가능 연산: +1, -1, *2
# number이 target이 되기 위한 최소 연산 횟수를 return

import queue

def solution(number, target):
    answer = 0
    visited = [0 for _ in range(10001)]
    q = queue.Queue()
    q.put(number)
    visited[number] = 1
    while not q.empty():
        x = q.get()
        if x == target:
            break
        if x + 1 <= 10000 and visited[x+1] == 0:
            visited[x+1] = visited[x]+1
            q.put(x+1)
        if x - 1 > 0 and visited[x-1] == 0:
            visited[x-1] = visited[x]+1
            q.put(x-1)
        if x*2 <= 10000 and visited[x*2] == 0:
            visited[x*2] = visited[x]+1
            q.put(2*x)
    answer = visited[target] - 1
    return answer