# Steps
# Initialize the Window: Start with an initial window at the beginning of the array.
# Expand/Slide the Window: Add new elements to the window.
# Shrink the Window: Remove elements from the window if necessary.
# Update the Result: Keep track of the best result or condition you need to check.

# Maximum Sum Subarray of Size k
def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i-(k-1)] #remove sum from window
    return max_sum

test_case_1 = [-2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(test_case_1, k))
# ** This can solve also with prefix sums(Think)