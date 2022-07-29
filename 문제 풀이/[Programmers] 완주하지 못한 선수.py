# level 1

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer += participant[i]
            return answer
        
    answer = participant[len(participant) - 1]
    
    return answer

# Hash 자료 구조를 이용한 풀이

def solution2(participant, completion):
    answer = ''
    hash_dict = {}
    # 1) hash(딕셔너리) 생성
    temp = 0
    for p in participant:
        hash_dict[hash(p)] = p
        # 2) p를 숫자로 변환한걸 key, p를 value로 만들어 {(key1:'p1'), (key2:'p2),..} 
        temp += int(hash(p))
        # 3) 각 key 값을 더함
    
    for c in completion:
        temp -= hash_dict(c)
        # 4) 완주한 사람의 key 값을 temp에서 하나씩 뺌
    answer = hash_dict[temp]
        # 5) 남아있는 숫자를 key로 가진 사람이 completion 목록에 없는 사람

    return answer