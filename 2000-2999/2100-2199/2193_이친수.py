# 2193 이친수
# 24.07.22
# Silver3
# Dynamic Programming


k = [0] * 91
k[1] = 1
k[2] = 1

for i in range(3, 91):
    k[i] = k[i - 1] + k[i - 2]

n = int(input())
print(k[n])
