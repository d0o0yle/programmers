n, m, k = map(int, input().split())

board = [[[] for _ in range(n)] for _ in range(n)]

dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

balls = []

for _ in range(m):
    r,c,ma,s,d = map(int, input().split())
    balls.append([r-1,c-1,ma,s,d])

for _ in range(k):
    # temp_balls = []
    # 이동
    while balls:
        r,c,ma,s,d = balls.pop(0)
        dx,dy = dirs[d]
        row = (r + s*dx + n) % n
        col = (c + s*dy + n) % n
        board[row][col].append([ma,s,d])

    for i in range(n):
        for j in range(n):
            count = len(board[i][j])
            # 2이상
            if count >= 2:
                sum_ma, sum_s, even_odd = 0, 0, 0
                while board[i][j]:
                    aBoard = board[i][j].pop(0)
                    sum_ma += aBoard[0]
                    sum_s += aBoard[1]
                    if aBoard[2] % 2 != 0:
                        even_odd += 1
                if even_odd == 0 or even_odd == count:
                    aDirs = [0,2,4,6]
                else:
                    aDirs = [1,3,5,7]
                if sum_ma // 5:
                    for aDir in aDirs:
                        balls.append([i,j,int(sum_ma/5),int(sum_s/count),aDir])
            # 1일 경우
            elif count == 1:
                balls.append([i,j] + board[i][j].pop())
print(sum([b[2] for b in balls]))
            

