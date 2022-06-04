import sys

s = int(input())

for x in range(s):
    f = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    arr.sort()
    print(arr)
    n, k = f[0], f[1]
    l_v, r_v = arr[0], arr[0]
    l, r, cout = 0, 0, 0
    strike = False
        
    while r < n:
        if arr[l] == arr[r]:
            print(f'count={cout}')
            cout += 1
            print(f'at {l} {arr[l]} == at {r} {arr[r]}, now count={cout}')
            if cout >= k:
                strike = True
                l_v, r_v = min(l_v,arr[l]), max(r_v,arr[r])
                l = r
            r += 1
        else:
            cout = 0
            l = r
            print(f'at {l} {arr[l]} != at {r} {arr[r]}, now count={cout}')
            
    if strike:
        print(f'{l_v} {r_v}')
    else:
        print(-1)
            

            