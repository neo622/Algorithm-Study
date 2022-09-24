# n x n 격자에 꽃이 피어있는 곳은 1로 표기된 리스트 주어짐
# 하루가 지나면 상하 좌우로 피는데 전체 다 피는 날은 며칠


n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

import queue

def solution(n, garden):
	q = queue.Queue()
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	for i in range(n):
		for j in range(n):
			if garden[i][j] == 1:
				q.put((i,j,0))
	while not q.empty():
		x, y, day = q.get()
		for k in range(4):
			mx = x+dx[k]
			my = y+dy[k]
			if mx >= 0 and mx < n and my >= 0 and my < n and garden[mx][my] == 0:
				garden[mx][my] += 1
				q.put((mx, my, day + 1))
				
	return day