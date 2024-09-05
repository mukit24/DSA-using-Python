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

# another approach
def seq_alt(nums, target):
    res = []
    def backtrack(index, curr, sum):
        if sum > target:
            return
        if sum == target:
            res.append(curr.copy())
        for i in range(index,len(nums)):
            curr.append(nums[i])
            sum += nums[i]

            backtrack(i+1, curr, sum)

            curr.pop()
            sum -= nums[i]
    backtrack(0, [], 0)
    return res
print('seq_alt', seq_alt([1,2,3], 3))

# modification(print just one ans)
def seq(nums, target):
    res = []
    # found = False
    def backtrack(index, curr, sum):
        # nonlocal found
        if sum == target:
            res.append(curr.copy())
            # found = True
            return True

        if index == len(nums):
            return
        curr.append(nums[index])
        sum += nums[index]
        # take
        if backtrack(index+1, curr, sum):
            return True
        # not take
        curr.pop()
        sum -= nums[index]
        if backtrack(index+1, curr, sum):
            return True
        

    backtrack(0,[],0)
    return res

print(seq([1,2,3], 3))

# modification(count number of answers)
# with apply optimization
def seq_count(nums, target):
    def backtrack(index, curr, sum):
        if sum == target:
            return 1
        if index == len(nums) or sum > target:
            return 0
        curr.append(nums[index])
        sum += nums[index]

        take = backtrack(index+1, curr, sum)
        curr.pop()
        sum -= nums[index]
        not_take = backtrack(index+1, curr, sum)
        return take+not_take
    return backtrack(0,[],0)
print(seq_count([1,2,3,4,5], 5))


    
