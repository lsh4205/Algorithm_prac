import sys

s = int(input())

for x in range(s):
    f = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    arr = arr.sort()
    n, k = f[0], f[1]
    l, l_v, r, r_v, cout = 0, arr[0], 0, arr[1], 1
    strike = Tru
        
    for i in range(n):
        if cout >= k:
            l_v, r_v = min(l_v,arr[l]), max(r_v,arr[r])
            strike = True 
            
        r = l+1
        if arr[l] == arr[r]:
            strike = True
            cout += 1
        else:
            strike = False
            cout = 1
            l = r
            
    if strike:
        print(f'{l_v} {r_v}')
    else:
        print(-1)
            

            