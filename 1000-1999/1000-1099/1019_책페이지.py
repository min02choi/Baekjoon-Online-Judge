# 23.10.01
# Gold1
# Unsolved

page_cnt = [0] * 10


n = int(input())

for page in range(1, n + 1):
    for i in str(page):
        # print(i)
        page_cnt[int(i)] += 1

print(page_cnt)
