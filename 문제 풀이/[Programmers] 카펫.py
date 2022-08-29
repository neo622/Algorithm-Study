# level 2
# 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
# 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return

def solution(brown, yellow):
    answer = []
    # 카펫의 넓이는 brown+yellow
    spec = brown + yellow
    # 가로 세로 경우의 수 중에서 조건을 걸어 완전 탐색
    for h in range(1, spec + 1):
        if spec % h == 0:
            w = spec // h
            if ((w-2)*(h-2) == yellow) and w >= h:
                answer.append((w,h))

    return answer[0]