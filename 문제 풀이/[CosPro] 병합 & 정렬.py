# 두개의 배열을 합쳐서 오름차순으로 정렬

def solution(arrA, arrB):
    ans = []
    Aidx = 0
    Bidx = 0
    while Aidx < len(arrA) and Bidx < len(arrB):
        if arrA[Aidx] < arrB[Bidx]:
            ans.append(arrA[Aidx])
            Aidx += 1
        else:
            ans.append(arrB[Bidx])
            Bidx += 1
    while Aidx < len(arrA):
        ans.append(arrA[Aidx])
        Aidx += 1
    while Bidx < len(arrB):
        ans.append(arrB[Bidx])
        Bidx += 1
    return ans
