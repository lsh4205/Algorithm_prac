import sys

s = int(input())

for i in range(s):
    n = int(input())
    arr = list(map(int, input().split()))
    
    l_p, r_p = 0, n-1
    l, r, cout = 0,0,0
    
    while l_p <= r_p:
        if l < r:
            l += arr[l_p]
            l_p += 1
        else:
            r += arr[r_p]
            r_p -= 1 
        if l == r:
            cout = l_p + (n - r_p) -1
    print(cout)
    # Lesson learned from this problem
    # First trial was good but need to code in a simple way
    # because I was confused by myself
    # because of additional condition