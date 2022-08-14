# 배열이 주어졌을 때, 증가(감소)-감소(증가)-증가(감소) 가 일어나는 연속적인 구간 중 가장 긴 부분 리스트의 길이를 return

def checking(s): # 증/감 을 체크한 리스트 생성
    INC = 1
    DEC = 0
    ret = [0 for _ in range(len(s))]
    ret[0] = -1 # 첫번째 값을 -1: 이전 숫자가 없기 때문
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            ret[i] = INC
        elif s[i] < s[i-1]:
            ret[i] = DEC
        else:
            ret[i] = -1
    
    return ret

def make_dp(c): # checking 함수를 통해 생성된 리스트를 통해 증감의 길이 기록
    ret = [0 for _ in range(len(c))]
    ret[0] = 1 # 증감의 최소는 2개 부터 -> 두번째 숫자는 무조건 증/감을 했으므로 첫번째 숫자는 1로 초기화
    for i in range(1, len(c)):
        if c[i] != c[i-1]:
            ret[i] += ret[i-1]+1
        else:
            ret[i] = 2 # 증가/감소가 연속으로 나오면 해당 숫자 2로 초기화
    return ret

def solution(arr):
    ans = 0
    check = checking(arr)
    dp = make_dp(check)
    ans = max(dp)
    if ans == 2:
        return 0
    return ans
