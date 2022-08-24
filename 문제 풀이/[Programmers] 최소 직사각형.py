# level 1
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            w.append(sizes[i][1])
            h.append(sizes[i][0])
    answer += max(w) * max(h)
    
    return answer
        