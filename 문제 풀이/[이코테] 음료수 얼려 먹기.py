# 0은 비어있는 부분, 1은 칸막이, 0이 붙어 있는 경우 연결되어있는 것으로 간주
# 0에 부어서 아이스크림을 만들 때, 생성되는 총 아이스크림 개수는?
# 예시에서는 총 3개 생성됨

n = 4
m = 5
graph = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,0,0,0]]

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문하는 함수
def dfs(x, y): # x->vertical, y -> horizontal
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 해당 노드가 0이면 1로 방문 처리하고 인접 노드에 대해 재귀적으로 dfs호출 
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y) # 상
        dfs(x + 1, y) # 하
        dfs(x, y - 1) # 좌
        dfs(x, y + 1) # 우
        return True
    # 해당 노드가 1이면 False
    return False


def solution(n, m):
    result = 0
    # 모든 노드에 대해 dfs함수 수행 후 결과가 True면 result 1 증가
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    return result
    # 정답 출력
