# 24.01.16
# Bronze2
# 구현
# 시간초과


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    num = a
    for j in range(b - 1):
        num = (num * a) % 10
    print(num)
