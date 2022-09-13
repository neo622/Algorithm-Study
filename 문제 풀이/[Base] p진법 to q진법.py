# p 진법으로 표현된 두개의 수를 더한 값을 q 진법으로 나타내어 return

s1 = "112001"
s2 = "12010"

def solution(s1, s2, p, q):
    answer = ''
    # int(str, 표현 진수) => 10진수로 바꿔줌
    sum = int(s1, p) + int(s2, p)

    # 10진법 수를 q진법 수로 변환
    # 10진법 수가 0이 될때 까지 q로 나누고 나머지를 answer에 저장
    while sum != 0:
        left = sum % q
        sum //= q
        answer += str(left)
    # 역순 출력해야 함
    return answer[::-1]
