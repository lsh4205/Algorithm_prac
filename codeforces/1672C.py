import sys
            
s = int(input())
for i in range(s):
	size = int(input())
	arr = list(map(int, input().split()))
	l, r = -1, -1
	for i in range(1, size):
		if arr[i] == arr[i-1]:
			if l == -1:
				l = i
			r = i
	if l == r:
		print(0)
	else:
		print(max(1, r - l - 1))
