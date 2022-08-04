# level 1 (kakao)

def solution(s):
    result = ''
    text = ''
    pad = ['zero','one','two','three','four','five','six','seven','eight','nine']
    dt = {}
    for i in range(len(pad)):
        dt[pad[i]] = i
        # {'zero' = 0, 'one' = 1, ...}
    for t in s:
        if t.isdigit():
            result += t
        elif t.isalpha:
            text += t
            if text in dt.keys():
                result += str(dt[text])
                text = ''
    return int(result)