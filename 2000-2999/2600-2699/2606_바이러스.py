# 2606 바이러스
# Silver3
# BFS(깊이 우선 탐색) 알고리즘
# 풀이 날짜: 2023-07-17


# 깊이 우선 탐색 알고리즘 정의
def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

n = int(input())
k = int(input())

visited = [False] * (n + 1)
com = [[] for i in range(n + 1)]
cnt = 0

# 그래프를 만드는 과정
for i in range(k):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)

dfs(com, 1, visited)
print(cnt)
