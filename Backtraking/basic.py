# Generating all possible binary strings of length n

def generate_binary_string(n):
    res = []
    def backtrack(cur_st):
        if  len(cur_st) == n:
            res.append(cur_st)
            return
        backtrack(cur_st+'0')
        backtrack(cur_st+'1')
    backtrack('')
    return res
print(generate_binary_string(2))

# sequence sum to target (similar to leetcode combination sum).
# [1,2,3,4] and target 4 then ans = [[4], [3,1]]

def seq(nums, target):
    res = []
    def backtrack(index, curr, sum):
        if sum == target:
            res.append(curr.copy())
            return

        if index == len(nums):
            return
        curr.append(nums[index])
        sum += nums[index]
        # take
        backtrack(index+1, curr, sum)
        # not take
        curr.pop()
        sum -= nums[index]
        backtrack(index+1, curr, sum)

    backtrack(0,[],0)
    return res

print(seq([1,2,3], 3))

