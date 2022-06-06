import sys

f = list(map(int, input().split()))
arr = list(map(int, input().split()))
# level
k = f[1]
# standard
x = f[2]

arr.sort()
count = 0
for i in range(1, len(arr)):
    if arr[i]-arr[i-1] > x:
        count += 1
print(count-k+1)