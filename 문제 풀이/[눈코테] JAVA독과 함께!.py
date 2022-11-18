# 돌의 내구도, 건너는 인원의 이름/점프력/몸무게 주어짐
# 항상 주어진 리스트의 순서대로 건넘
# 생존자 출력

rock = [1, 2, 1, 4]
people = [["ruby", "3", "4"], ["Pitch", "3", "3"], ["C","2","1"], ["Cobol","1","1"]]

def solution(rock, people):
    name = [p[0] for p in people]
    for i in people:
        rock_idx = 0
        while rock_idx < len(rock):
            rock_idx += (int(i[1]))-1
            rock[rock_idx] -= int(i[2])
            if rock[rock_idx] < 0:
                name[name.index(i[0])] = "fail"
                break

    return rock


