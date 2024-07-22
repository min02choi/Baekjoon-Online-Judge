# 24.07.10
# Silver2


t = int(input())

while(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(n)] for _ in range(m)]

    while(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    new_field = field

