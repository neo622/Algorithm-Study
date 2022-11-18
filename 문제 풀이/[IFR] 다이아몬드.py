# arr에서 다이아몬드 모양의 전체 합

arr = [
    [10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]
]

def solution(arr):
    ans = []
    mid = len(arr)//2
    l, r = len(arr[0])//2, len(arr[0])//2
    for i in range(mid+1):
        ans.append(sum(arr[i][l:r+1]))
        l -= 1
        r += 1
    
    l += 2 #1
    r -= 2 #3
    
    for j in range(mid+1, len(arr)):
        ans.append(sum(arr[j][l:r+1]))
        l += 1
        r -= 1
        
    return sum(ans)