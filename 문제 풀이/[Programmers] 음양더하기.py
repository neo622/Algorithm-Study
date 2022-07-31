# level 1

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = absolutes[i] * -1
        else:
            continue
    answer = sum(absolutes)
    return answer

# 일단 풀어서 올렸지만..앞으로는 어려운걸 풀어봐야겠다