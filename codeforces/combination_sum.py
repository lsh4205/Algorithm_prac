def combinationSum(candidates, target):
    result = []
    helper(candidates, [], target, result)
    return result
                
def helper(candidates, path, left, result):
    print(f'Before for loop: {left}')
    if left == 0:
        result.append(path)
        return
    elif left < 0:
        return
    else:
        i = 0
        while left >= 0 and i < len(candidates):
            print(f'Left = {left}, cur = {candidates[i]}')
            helper(candidates, path + [candidates[i]], left - candidates[i], result)
            i += 1

print(combinationSum([2,3,5], 8))
print(combinationSum([2,3,6,7], 7))