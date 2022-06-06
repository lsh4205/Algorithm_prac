import sys

s = int(input())

for x in range(s):
    f = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    arr.sort()
    k = int(f[1])
    # Count repeated elements in the dict
    counted_arr = dict((i, arr.count(i)) for i in arr)
    arr = []
    
    # Then, delete the element which are not repeated enough
    for x in counted_arr:
        if counted_arr[x] >= k:
            arr.append(x)
    if len(arr) == 0:
        print(-1)
    else: 
        l = arr[0]
        l_v, r_v = arr[0], arr[0]
        max_v = 0
        for i in range(1, len(arr)):
            # If (current_index_value)-1 is equal to previous index value,
            # it means it is consecutive 
            if arr[i-1] == arr[i]-1:
                if arr[i]-l > max_v:
                    l_v = l
                    r_v = arr[i]
                    max_v = arr[i]-l
            else: 
                l = arr[i]
        print(f'{l_v} {r_v}')
            
# Cause TLE on the test6 
# When the value of n is large (usually larger than 10^5)
# then because there can be high number of collisions so hashmaps gives
# its worst case time complexity for insertion operations
# that is O(n) and not O(1) which is why the overall time complexity becomes O(n^2).

# The solution is to use a map as
# there we don't have a problem of collisions
# and the time complexity is logn per operation.
            