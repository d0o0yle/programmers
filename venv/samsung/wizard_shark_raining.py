N, M = map(int, input().split())

def compute(n):
    while n not in range(1,N+1):
        if n < 1:
            n += N
        elif n > N:
            n -= N
    return n

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

clouds = [(N, 1), (N, 2), (N-1, 1), (N-1, 2)]

dirs = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

for _ in range(M):
    d, s = map(int, input().split())
    # move
    temp_clouds = []
    visited = [[False] * N for _ in range(N)]
    for x, y in clouds:
        nx = compute(x + (dirs[d][0]*s))
        ny = compute(y + (dirs[d][1]*s))
        temp_clouds.append([nx, ny])
        visited[nx-1][ny-1] = True

    # rain
    for x, y in temp_clouds:
        x -= 1
        y -= 1
        board[x][y] += 1

    for x, y in temp_clouds:
        x -= 1
        y -= 1
        dlist = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for dx, dy in dlist:
            nx = x + dx
            ny = y + dy
            if nx in range(N) and ny in range(N):
                if board[nx][ny] != 0:
                    board[x][y] += 1

    clouds.clear()

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and board[i][j] >= 2:
                clouds.append([i+1,j+1])
                board[i][j] -= 2
answer = 0
for row in board:
    answer += sum(row)
print(answer)