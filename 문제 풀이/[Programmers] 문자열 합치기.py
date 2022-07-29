def solution(s):
    result=[]
    if len(s)==1:
        return 1
    for i in range(1, (len(s)//2)+1):
        # out of range 방지
        b = ''
        cnt = 1
        case=s[:i]

        for j in range(i, len(s), i):
            if case==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b + str(cnt)+case
                else:
                    b = b + case
                case=s[j:j+i]
                cnt = 1
        if cnt!=1:
            b = b + str(cnt) + case
        else:
            b = b + case
                
        result.append(len(b))
    return min(result)
