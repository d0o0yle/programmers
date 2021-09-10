from collections import deque

def valid(row, col):
    return row in range(5) and col in range(5)

# p는 시작점
def bfs(place):
    pList = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                pList.append([i, j])

    for p in pList:
        # 큐에는 초기 값
        queue = deque([p])

        # 방문 처리 리스트
        visited = [[0]*5 for _ in range(5)]

        # 경로 길이 리스트
        distance = [[0]*5 for _ in range(5)]

        visited[p[0]][p[1]] = 1

        while queue:
            dist = [(0,1), (1,0), (0,-1), (0,1)]

            x, y = queue.popleft()
            for dx, dy in dist:
                nx = x + dx
                ny = y + dy
                if valid(nx, ny) and visited[nx][ny] == 0:
                    # O 만나면 계속 고고
                    if place[nx][ny] == 'O':
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                    # P 만났는데 맨해튼 거리 2보다 작으면 거리두기 실패!
                    elif place[nx][ny] == 'P' and distance[x][y] < 2:
                        return 0
    # 모든 점에 대해 거리두기 성공
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer

if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    results = [1, 0, 1, 1, 1]

    print('->', solution(places), results)
