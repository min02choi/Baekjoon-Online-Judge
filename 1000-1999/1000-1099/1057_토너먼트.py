# 24.01.30
# Silver4
#
#

# 반을 쪼개서 더 많은 쪽 아닌가
# 크게 반을 쪼갰는데 다른쪽이다 -> 2^n승 의 n
# 크게 반을 쪼갰는데 같은쪽이다 -> 쪼개기 계속

# 1, 2, | 3, 4, | 5, 6, | 7, 8, | 9, 10 | 11 12 | 13 14 | 15 16 | 17
# 아 씨바 개짜증나네
n, kim, lim = map(int, input().split())

cnt = 0
num = n // 2
bar = num
if num % 2 == 1:
    num -= 1

while True:
    if kim <= bar and lim <= bar:
        cnt += 1
        num //= 2
        bar = num
        if num % 2 == 1:
            num -= 1
    if kim > bar and lim > bar:
        cnt += 1
        bar = bar + num//2
        if num % 2 == 1:
            num -= 1
    else:
        break

top = 0
while 2**top < n:
    top += 1

# top -= 1

# round = 2**(top - num)
round = top - cnt

print(round)

"""
# tqtqtqtqt
num = n // 2
while num > 1:
    # pass
    if kim <= num and lim <= num:
        num //= 2
        if num % 2 == 1 and num > 1:
            num -= 1
    else:
        break       # 다른 쪽일 때

# round = 1
# while 2**round < num * 2:
#     round += 1

num -= 1
full = 1
while 2**full < n:
    full += 1
full -= 1

round = 2**(full - num)

print(round)
"""

# 1000 20 31
# 500
# 250
# 125 -> 124
# 62
# 31 -> 30 : 같은 쪽 마지막
# 15 -> 다른쪽임 -- 2^n 값이 넘어가는 바로 그 다음 n == 4

# 60000 101 891
# 30000, 15000, 7500, 3750, 1875, 937
# 468 - 다른쪽임

# 2 4 8 16 32 64 128 256 512


