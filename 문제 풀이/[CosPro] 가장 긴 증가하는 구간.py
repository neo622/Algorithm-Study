def solution(arr):
    answer = 0
    pos = [1 for i in range(len(arr))]

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            pos[i] = pos[i-1]+1
        else:
            continue
    
    answer = max(pos)

    return answer
