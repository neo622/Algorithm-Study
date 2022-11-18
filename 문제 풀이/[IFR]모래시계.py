arr = [
    [10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]
]
move = [[2,0,3],[5,1,2],[3,1,4]]
# move읽어서 배열 변경하고[행, 0왼쪽/1오른쪽, 이동횟수]
# arr에서 모래시계 모양으로 전체 합

def solution2(arr, move):
    ans = []
    # 배열 회전
    for m in move:
        # 왼쪽 회전
        if m[1] == 0:
            for _ in range(m[2]):
                x = arr[m[0]-1].pop(0)
                arr[m[0]-1].append(x)
        # 오른쪽 회전
        else:
            for _ in range(m[2]):
                y = arr[m[0]-1].pop()
                arr[m[0]-1].insert(0,y)

    # 모래시계 모양 구하기            
    l, r = 0, len(arr[0])
    mid = len(arr)//2
    for i in range(mid+1):
        ans.append(sum(arr[i][l:r]))
        l += 1
        r -= 1
    l, r = len(arr[0])//2, (len(arr[0])//2)+1 #2, 3 
    for j in range(mid+1, len(arr)):
        ans.append(sum(arr[j][l-1:r+1])) #[1:4]
        l -= 1
        r += 1
    return sum(ans), arr
        