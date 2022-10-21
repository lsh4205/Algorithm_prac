import sys

s = int(input())
for x in range(s):
    a = input()
    i, j = 0, len(a)-1
    while i <= j:
        if a[i] == a[j]:
            i += 1
            j -= 1
        elif a[i+1] == a[j]:
            i += 1
        elif a[i] == a[j-1]:
            j -= 1
        
        # 1. if the palindrome len is divided by 2

        # 2. if the palindrome len is not divided by 2

    