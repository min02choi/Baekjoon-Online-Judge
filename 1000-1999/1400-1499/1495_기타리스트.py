# 1495 기타리스트
# 24.07.23
# 다이나믹 프로그래밍


N, S, M = map(int, input().split())
vol = list(map(int, input().split()))
vol.insert(0, 0)

cur_vol = set()

flag = 0
cur_vol.add(S)

for i in range(1, N + 1):
    next_vol = set()
    for j in cur_vol:
        if (0 <= j - vol[i] <= M):
            next_vol.add(j - vol[i])
        if (0 <= j + vol[i] <= M):
            next_vol.add(j + vol[i])
    if not next_vol:
        flag = 1
        break
    cur_vol = next_vol

if flag == 1:
    print(-1)
else:
    print(max(cur_vol))
