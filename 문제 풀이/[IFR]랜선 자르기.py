# 랜선 자르기 
# 랜선을 N개 이상으로 만들고 싶을 때 자르는 최대 길이
lan = [802, 743, 457, 539]
N = 11

def solution(lan, N):
    ans = 0
    K = len(lan)
    x = min(lan)
    while True:
        for l in lan:
            ans += (l // x)
        if ans < N:
            x -= 1
            ans = 0
        else:
            break
    return x


