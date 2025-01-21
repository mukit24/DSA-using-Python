'''
Recursion is when a function calls itself to solve a smaller version of the original problem until a base condition is met.

Key Components of Recursion:
1. Base Case: The stopping condition that prevents infinite recursion. (What is the simplest version of the problem?)
2. Recursive Case: The logic that breaks the problem into smaller sub-problems. (Think about how you can reduce the problem into smaller subproblems.)

Now take a simple example: Sum of a list. [2,3,4].(See code below).
Base Case: If the list is empty, return 0. (The sum of an empty list is 0.)
Recursive Case: The sum of a list is the first element plus the sum of the rest of the list.

Why Does Recursion Feel Difficult?
Abstract Thinking: Recursion often requires you to think about the problem as a whole and trust that the smaller parts will work.
Visualization: Its hard to track recursive calls mentally.

How to Master Recursion?
Start Small: Practice simple problems like factorial, Fibonacci, or reversing a string.
Dry Run: Write down the recursive calls for a small input to see how the problem breaks down.
Draw Call Stack: Visualize how functions are called and returned.
Debug: Use print statements to trace how the function is executed.

'''

#sum of a list
def sumList(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sumList(nums[1:])
print('Sum of List', sumList([2,3,4]))

# Factorial (Idea: Fact of 5 = 5 * fact(4))
def fact(num):
    if num <= 1:
        return 1
    return num * fact(num-1)
print('Factorial', fact(5))

# reverse string (First character + rev(st[1:]))
def reverseString(st):
    if len(st) <= 1:
        return st
    return reverseString(st[1:]) + st[0]

print('Reverse String', reverseString('Hello'))

# pallindrome (idea: How to break this into smaller similar problem? A string is pallindrome if First & Last Character is same and Middle are also Pallindrome)
def isPallindrome(st):
    if len(st) <= 1:
        return True
    if st[0] == st[-1]:
        return isPallindrome(st[1:len(st)-1])
    return False    
print(isPallindrome('nayan'))

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