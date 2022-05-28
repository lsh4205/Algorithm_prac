import sys

s = int(input())

for i in range(s):
    size = int(input())
    arr = list(map(int, input().split()))
    
    l, r = arr[0], arr[size-1]
    l_p, r_p = 1, size-2
    last_l, last_r = -1, -1
    
    while l_p <= r_p:
        if l == r:
            last_l = l_p
            last_r = r_p
        if l < r:
            l += arr[l_p]
            l_p += 1
        else:
            r += arr[r_p]
            r_p -= 1     

    if l == r:
        print(l_p + size-1 - r_p)
    else:
        if last_l != -1:
            print(last_l + size-1 - last_r)
        else:
            print(0)
