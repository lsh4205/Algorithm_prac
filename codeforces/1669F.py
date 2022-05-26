import sys

s = int(input())

for i in range(s):
    size = int(input())
    arr = list(map(int, input().split()))
    
    l, r = arr[0], arr[size-1]
    l_p, r_p = 1, size-2
    
    while l_p < size-2 and r_p > 1:
        if l < r:
            l += arr[l_p+1]
            l_p += 1
        else:
            r += arr[r_p-1]
            r_p -= 1
    print(f'{l_p}, {r_p}')       
    if l_p >= r_p:
            if l == r:
                print(l_p-0 + size-1-r_p)
            else:
                print(0)
