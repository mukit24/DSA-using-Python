# Bubble Sort O(n^2)
case1 = [3,6,1,78,3,23,56,21,13,9,54]

def bubble_sort(arr):
    for _ in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# print(bubble_sort(case1))

# Insertion Sort O(n^2)
# need less swapping

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort(case1))