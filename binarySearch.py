def binarySearch(nums, target):
    return recursion(nums, target)

def recursion(nums, target):
        print(nums)
        middle = int(len(nums)/2)
        print(middle)
        if middle == 0:
            if nums[middle] != target:
                return -1
        if nums[middle] == target:
            return middle 
        if nums[middle] > target:
            print(f' {nums[middle] } > {target}')
            return middle - recursion(nums[0: middle], target)
        else:
            print(f' {nums[middle] } < {target}')
            return recursion(nums[middle: len(nums)], target) + middle

def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r :
        m = int((l+r) / 2)
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
    return -1

nums1 = [-1,0,3,5,9,12]
target1 = 9
target2 = 2
target3 = -1

print(search(nums1, target1))
print(search(nums1, target2))
print(search(nums1, target3))