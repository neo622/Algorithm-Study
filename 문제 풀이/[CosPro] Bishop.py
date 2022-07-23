# 여러개의 비숍 위치가 주어졌을 때 비숍에게 잡히지 않는 칸 개수 리턴
def solution(bishops):
	answer = 0
	chess_map = [[1 for _ in range(8)] for _ in range(8)]
	for b in bishops:
		x = ord(b[0]) - ord('A')
		y = int(b[1]) - 1
		chess_map[y][x] = 0

		dx = x - 1
		dy_up = y
		dy_dn = y
		while dx >= 0:
			dy_up = dy_up + 1
			dy_dn = dy_dn - 1
			if dy_up < 8:
				chess_map[dy_up][x] = 0
			if dy_dn >= 0:
				chess_map[dy_dn][x] = 0
			dx -= 1
            
        dx = x + 1
		dy_up = y
		dy_dn = y
		while dx < 8:
			dy_up = dy_up + 1
			dy_dn = dy_dn - 1
			if dy_up < 8:
				chess_map[dy_up][dx] = 0
			if dy_dn >= 0:
				chess_map[dy_dn][dx] = 0
			dx += 1
	for i in chess_map:
		answer += i.count(1)

	return answer
