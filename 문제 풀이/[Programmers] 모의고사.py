# level 1
# 정답 번호 리스트가 주어졌을 때 3명의 학생이 문제를 찍는 방식에 따라 가장 많이 맞힌 학생 return

def solution(answers):
    answer = []
    users = [1, 2, 3]
    u1 = [1,2,3,4,5]
    u2 = [2,1,2,3,2,4,2,5]
    u3 = [3,3,1,1,2,2,4,4,5,5]
    count1, count2, count3 = 0, 0, 0
    while len(answers) >= len(u1):
        u1 += u1
        u2 += u2
        u3 += u3
    for i in range(len(answers)):
        if answers[i] == u1[i]:
            count1 += 1
        if answers[i] == u2[i]:
            count2 += 1
        if answers[i] == u3[i]:
            count3 += 1
    ans = [count1, count2, count3]
    for check in range(len(ans)):
        if max(ans) == ans[check]:
            answer.append(users[check])
    return answer 