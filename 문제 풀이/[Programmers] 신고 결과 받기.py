def solution(id_list, report, k):
    answer = []
    answer_board = [[0, i] for i in id_list]
    pad = [0] * len(id_list)
    board = []
    for i, j in zip(id_list, pad):
        board.append([i,j])
    for r in report:
        reported = r.split()[1]
        reporter = r.split()[0]
        for check in board:
            if (reported == check[0]) and (reporter not in check):
                check[1] += 1
                check.append(reporter)
    
    for ans in board:
        if ans[1] >= k:
            for a in ans[2:]:
                for l in answer_board:
                    if l[1] == a:
                        l[0] += 1
    for b in answer_board:
        answer.append(b[0])
        
    return answer