# 왼쪽 맨 위에서 오른쪽 맨 아래로 이동
# 1 인 곳만 갈 수 있음
# 최단 경로 return

# BFS 알고리즘 문제
# 모든 길(1)에 대해 BFS를 수행하여 시작 노드에서 해당 길 까지의 거리를 1을 더해서 구함

from collections import deque

n, m = 5, 6
graph = [[1,0,1,0,1,0],
         [1,1,1,1,1,1],
         [0,0,0,0,0,1],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1]]

def bfs_solution(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append(x,y)
    # queue 가 빌 떄 까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나는 경우 무시
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 벽(0)인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

