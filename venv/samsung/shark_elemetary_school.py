N = int(input())

friendNum = N*N
friendList = [0]*(friendNum+1)

board = [[0]*N for _ in range(N)]

# print(board)

for _ in range(friendNum):
    a, b, c, d, e = map(int, input().split())
    friendList[a] = [b,c,d,e]

    candidate = 0
    emptyCnt = 0
    friendCnt = 0
    dlist = [(0,1),(1,0),(-1,0),(0,-1)]

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            ecnt = 0
            fcnt = 0
            for dx, dy in dlist:
                nx = i + dx
                ny = j + dy
                if nx in range(N) and ny in range(N):
                    if board[nx][ny] == 0:
                        ecnt += 1
                    elif board[nx][ny] in friendList[a]:
                        fcnt += 1
            if fcnt > friendCnt:
                candidate = [i, j]
                friendCnt = fcnt
                emptyCnt = ecnt
            elif fcnt == friendCnt:
                if ecnt > emptyCnt:
                    candidate = [i, j]
                    emptyCnt = ecnt
                elif ecnt == emptyCnt:
                    if candidate == 0:
                        candidate = [i, j]
    # print(a, "->",candidate)
    x, y = candidate
    board[x][y] = a

answer = 0

for i in range(N):
    for j in range(N):
        numFri = 0
        dlist = [(0,1), (1,0),(0,-1),(-1,0)]
        for dx, dy in dlist:
            nx = i + dx
            ny = j + dy
            if nx in range(N) and ny in range(N):
                if board[nx][ny] in friendList[board[i][j]]:
                    numFri += 1
        if numFri == 1:
            answer += 1
        elif numFri == 2:
            answer += 10
        elif numFri == 3:
            answer += 100
        elif numFri == 4:
            answer += 1000
print(answer)
