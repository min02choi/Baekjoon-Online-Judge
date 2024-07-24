# 2579 계단오르기
# 24.07.24

# 첫 칸에서 시작하는 경우
# 두 번째 칸에서 시작하는 경우


n = int(input())

stair = [int(input()) for i in range(n)]
stair.insert(0, 0)

if n <= 3:
    if n == 1:
        print(stair[1])
    if n == 2:
        print(stair[1] + stair[2])
    if n == 3:
        print(max(stair[1] + stair[3], stair[2] + stair[3]))
    exit()

dp = [0] * (n + 1)
dp[1] = stair[1]
dp[2] = max(stair[1] + stair[2], stair[2])
dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[-1])
