import sys

s = int(input())
print(s)
for i in range(s):
    size = int(input())
    arr = list(map(int, input().split()))
    
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    
    print(sum)
        
    if sum%2 == 1:
        print(0)
    else:
        equal = int(sum/2)
        count =0
        for i in range(size):
            if equal == 0:
                print(count)
            else:
                equal -= arr[i]
                count += 1
