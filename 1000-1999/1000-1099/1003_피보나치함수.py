# 24.07.22
# 다이나믹 프로그래밍


fib01 = {0: [1, 0],
         1: [0, 1]}

for i in range(2, 41):
    fib01[i] = [fib01[i-1][0] + fib01[i-2][0], fib01[i-1][1] + fib01[i-2][1]]

t = int(input())
for i in range(t):
    n = int(input())
    print(fib01[n][0], fib01[n][1])
