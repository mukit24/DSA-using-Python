# if duplicate then return 1st
# if not found then return -1

# Binary Search Time Complexity O(logn)
# Each iteration whole array is divided into half like n/2, n/4... untill its 1.
# So, n/2^k = 1 then 2^k = n, So, k = logn.

#assume these cases as assending order
test_case_1 = [-3,-2,-1]
test_case_2 = [2,2,4,5,7,7,7,8,10]
test_case_3 = []

def linear_search(case, target):
    for i in range(0,len(case)-1):
        if case[i] == target:
            return i
    return -1

print('linear search', linear_search(test_case_3, 4))

def binary_search_basic(case, target):
    lo = 0
    hi = len(case)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        # print(lo,hi,mid)
        if case[mid] == target:
            return mid
        elif case[mid] > target:
            hi = mid -1
        else:
            lo = mid + 1
    return -1

print('basic_binary_search',binary_search_basic(test_case_2, 2))

# not giving correct result for case 2 in that scenerio
# so we need a helper function that defines the condition
def binary_search_with_extra_contidion(case, target):
    lo = 0
    hi = len(case)-1
    while lo <= hi:
        mid = (lo + hi) // 2

        if case[mid] == target:
            position = locate_position(case, mid, target)
            if position == 'found':
                return mid
            else:
                hi = mid - 1
        elif case[mid] > target:
            hi = mid -1
        else:
            lo = mid + 1
    return -1

def locate_position(case, mid, target):
    if mid > 0 and case[mid-1] == target:
        return 'left'
    else:
        return 'found'

print('with extra condition', binary_search_with_extra_contidion(test_case_2, 2))
    