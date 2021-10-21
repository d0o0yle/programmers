n, q = map(int, input().split())
ln = 2**n
board = [list(map(int, input().split())) for _ in range(ln)]
levels = list(map(int, input().split()))

def rotate(table):
    n = len(table)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = table[n-j-1][i]
    return result

for l in levels:
    k = 2**l
    for i in range(0,ln,k):
        for j in range(0,ln,k):
            # 자르고 회전
            temp = [[0]*k for _ in range(k)]
            for r in range(i, i+k):
                for c in range(j, j+k):
                    temp[r-i][c-j] = board[r][c]
            rot = rotate(temp)

            # 다시 넣어주기
            for r in range(i, i + k):
                for c in range(j, j + k):
                    board[r][c] = rot[r-i][c-j]

    check = [[0]*ln for _ in range(ln)]

    # 회전 후 녹일 얼음 체크
    for x in range(ln):
        for y in range(ln):
            if board[x][y] == 0:
                continue
            d = [(0,1),(1,0),(-1,0),(0,-1)]
            nonzero = 0
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if nx in range(ln) and ny in range(ln) and board[nx][ny]:
                    nonzero += 1
            if nonzero < 3:
                check[x][y] = 1
    # 얼음 녹이기
    for x in range(ln):
        for y in range(ln):
            if check[x][y]:
                board[x][y] -= 1

# 2가지 구하기
# 남아있는 얼음 합
# 가장 큰 덩어리 칸 개수
visited = [[False]*ln for _ in range(ln)]

total = 0
max_ice = 0
for i in range(ln):
    for j in range(ln):
        if not visited[i][j] and board[i][j]:
            cnt = 0
            d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            queue = [(i,j)]
            visited[i][j] = True
            total += board[i][j]
            while queue:
                x, y = queue.pop(0)
                cnt += 1
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    if nx in range(ln) and ny in range(ln) and not visited[nx][ny] and board[nx][ny]:
                        queue.append((nx,ny))
                        visited[nx][ny] = True
                        total += board[nx][ny]
            max_ice = max(max_ice, cnt)
print(total)
print(max_ice)

