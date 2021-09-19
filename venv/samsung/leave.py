# DP 이용...

def solution():
    N = int(input())
    T = []
    P = []
    dp = []
    for _ in range(N):
        time, price = map(int, input().split())
        T.append(time)
        P.append(price)
        dp.append(price)
    dp.append(0)

    for i in range(N-1, -1, -1):
        if i + T[i] > N:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
    print(dp[0])

if __name__ == '__main__':
    solution()