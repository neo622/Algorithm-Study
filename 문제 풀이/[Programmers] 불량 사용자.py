# level 3

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

from itertools import product

def solution(user_id, banned_id): 
    answer_matrix = []
    match = []
    for ban in banned_id: 
        # 1) banned_id를 기준으로 해당 원소를 통해 정지당할 수 있는 user id를 이차원 리스트로
        matched = []
        for user in user_id:
            if len(user) != len(ban):
                continue
            else:
                is_same = True
                for b,u in zip(ban, user):
                    if b != '*' and b != u:
                        is_same = False
                if is_same:
                    matched.append(user)
        match.append(matched) 
        # 2) match = [['frodo', 'crodo'], ['frodo', 'crodo'], ['abc123', 'frodoc']]
        
    board = list(product(*match))
        # 3) itertools의 product를 이용해 이차원 리스트 원소 조합 생성
        # board = [('frodo', 'frodo', 'abc123'), ('frodo','frodo','frodoc'), ...]
    for lst in board:
        if len(lst) != len(set(lst)):
            continue
        else:
            answer_matrix.append(lst)
        # 4) board의 원소 중 중복 항목이 있는 원소 이외의 원소를 answer_matrix에 append
    
    
    return len(set([tuple(set(ans)) for ans in answer_matrix]))
        # 5) 이차원 리스트 중복 제거(구성요소) 후 리스트 길이 return

