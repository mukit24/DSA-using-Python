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

# merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        

        i=j=k=0
        # print(left,right,k)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

nums = [5,3,7,2,-1,10,7]
merge_sort(nums)
print(nums)