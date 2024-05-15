# here is a sorted_list = [2,3,5,7,9,10]
# if rotating 2 times then [9,10,2,3,5,7]
# if 5 times [3,5,7,9,10,2]
# edge case can be emtpt and if rotate n times then we get the orginal list

# find minimum number of rotations in a sorted rotated list, assume all are unique

# first fact is the minimum number's position is the answer, here the sorting interrupted.
# minimum number's previous number will be greater than
# can be solve easily by linear search using this fact
# for binary search:
# 1. if mid's previous is greater then return position
# 2. if not, then check last element. if it is greater than mid that means we can not find solution in right half.(see line 2 with add extra one element).
# 3. so solution lies in left half. change the hi position to mid - 1.
# 4. if mid > last element. then search in the right half and change lo=mid+1
# 5. Repeat untill 1

def minimum_rotations(nums):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo+hi) // 2
        # print(mid)
        if mid > 0 and nums[mid-1] > nums[mid]:
            return mid
        if nums[-1] > nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return 0 #bcz num of rotations

case_1 = [3,5,7,9,10,2] 
print(minimum_rotations(case_1))

# see leetcode.txt for improved logic
