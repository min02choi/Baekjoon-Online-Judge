def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == target):
            return 1
        elif (arr[mid] > target):
            high = mid - 1
        else:
            low = mid + 1
    return 0


n = int(input())
A = [int(m) for m in input().split()]
m = int(input())
M = [int(m) for m in input().split()]

A.sort()

for i in range(len(M)):
    print(binary_search(A, M[i]))