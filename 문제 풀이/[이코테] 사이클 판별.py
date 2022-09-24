# 사이클이 발생하는 순번 return

n = 3
connections = [[1, 2], [1, 3], [2, 3]]

# 부모 노드가 value면 value return하고, 아니라면 타고 올라가서 부모 노드 찾음
def find(parent, v):
    if parent[v] == v:
        return v
    parent[v] = find(parent, parent[v])
    return parent[v]

# 두 수는 연결 되어있으므로, 부모노드를 같게 만들고 부모 노드가 같다면 사이클이 발생한 것이므로 True 
def merge(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return True
    parent[a] = b
    return False

def solution(n, connections):
    ans = 0
    parent = [i for i in range(n+1)]
    for i, conn in enumerate(connections):
        # 사이클이 발생하면 해당 순번 + 1
        if merge(parent, conn[0], conn[1]):
            ans = i + 1
            break
    return ans