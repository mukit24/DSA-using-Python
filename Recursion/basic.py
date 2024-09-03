# reverse string
def reverseSring(st):
    # print(st)
    if not st:
        return ''
    return reverseSring(st[1:]) + st[0]

print(reverseSring('Hello'))

# pallindrome
def isPallindrome(st):
    if len(st) == 0 or len(st) == 1:
        return True
    if st[0] == st[-1]:
        return isPallindrome(st[1:len(st)-1])
    return False

print(isPallindrome('kaya'))

# sum to certain value

def sum(num):
    if num == 0:
        return 0
    return num + sum(num-1)

print(sum(4))

# Binary Search Recursion

def binary_search(nums,left, right, target):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    
    if nums[mid] < target:
        return binary_search(nums, mid+1, right, target)
    return binary_search(nums, left, mid-1, target)

print(binary_search([1,2,3,4], 0, 3, 2))

# fibonacchi series

def fibo(num):
    if num==0 or num == 1:
        return num
    return fibo(num-1)+fibo(num-2)

print(fibo(6))