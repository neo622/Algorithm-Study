# 현재 게시글 번호가 매개 변수로 주어짐
# 조건1. 현재 게시글보다 커야함
# 조건2. 자릿 수가 짝수여야 함
# 조건3. 자릿 수가 2n일 때, 앞 n자리 수의 합과 뒤 n자리 수의 합이 같음
# 조건이 다음과 같을 때 당첨되려면 게시글을 몇개 더 써야 하는지 return

def count_len(n):
    ret = 0
    while n > 0:
        ret += 1
        n //= 10
    return ret

def devider(length):
    ret = 0
    while length > 0:
        ret *= 10
        length //= 10
    return ret

def each_sum(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

def solution(num):
    next_num = num
    while True:
        next_num += 1
        length = count_len(next_num)
        if length % 2 != 0:
            continue
        dev = devider(length // 2)
        front = next_num // dev
        back = next_num % dev
        front_sum = each_sum(front)
        back_sum = each_sum(back)
        if front_sum == back_sum:
            ans  = (next_num - num)
            break
    return ans
    





