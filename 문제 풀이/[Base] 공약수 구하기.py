# a, b, c의 공약수의 개수를 구하기

# 두 수의 최대 공약수를 구하는 함수
# a > b일 때, a와 b의 최대 공약수는 a를 b로 나눈 나머지
def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def solution(a, b, c):
    answer = 0
    gcd_three = gcd(gcd(a,b), c)
    for i in range(1, gcd_three+1):
        if gcd_three % i == 0:
            answer += 1
    return answer
