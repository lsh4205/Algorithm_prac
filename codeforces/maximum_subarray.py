def maximumSubarray1(nums):
    def helper(l, r):
        mid = (l+r)//2
        high = 0
        if l == r: 
            return [l,l]
        # left is bigger?
        # right is bigger?
        # left + right is bigger?
        l_res = helper(l, mid)
        r_res = helper(mid+1, r)

        sum_left_right = sum(nums[l_res[0]:r_res[1]+1])
        sum_left = sum(nums[l_res[0]:l_res[1]+1])
        sum_right = sum(nums[r_res[0]:r_res[1]+1])
        print(f's_l_r = {l_res[0],r_res[1]} {sum_left_right}, s_l = {l_res[0],l_res[1]} {sum_left}, s_r = {r_res[0],r_res[1]} {sum_right}')
        if sum_left_right > sum_left and sum_left_right > sum_right:
            print(f'Left + Right : {[l_res[0], r_res[1]]}')
            return [l_res[0], r_res[1]]
        elif sum_left > sum_left_right and sum_left > sum_right:
            print(f'Left : {l_res}')
            return l_res
        else:
            print(f'Right : {r_res}')
            return r_res
    res = helper(0, len(nums)-1)
    print(res)
    return sum(nums[res[0]:res[1]+1])

def maximumSubarray(nums):
    local_max = global_max = nums[0]
    for num in nums[1:]:
        print(f'local: {local_max}, num: {num}, +: {num+local_max}, gl: {global_max}')
        local_max = max(num + local_max, num)
        global_max = max(local_max, global_max)
    return global_max

print(maximumSubarray([4,-1,2,1]))
print(maximumSubarray([-2,1,-3, 4,-1,2,1, -5,4]))
print(maximumSubarray([1,2,-1]))
print(maximumSubarray([5,4,-1,7,8]))
        