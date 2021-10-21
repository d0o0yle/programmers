from collections import deque

n, k = map(int, input().split())

convey = deque(list(map(int, input().split())))
robot = deque([0] * n)

round = 0

while convey.count(0) < k:
    convey.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(n-2, -1, -1):
            if convey[i+1] and not robot[i+1] and robot[i]:
                convey[i+1] -= 1
                robot[i] = 0
                robot[i+1] = 1
            robot[-1] = 0

    if convey[0] and not robot[0]:
        robot[0] = 1
        convey[0] -= 1
    round += 1
print(round)