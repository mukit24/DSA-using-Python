# Steps
# Initialize the Window: Start with an initial window at the beginning of the array.
# Expand/Slide the Window: Add new elements to the window.
# Shrink the Window: Remove elements from the window if necessary.
# Update the Result: Keep track of the best result or condition you need to check.

# Maximum Sum Subarray of Size k
def max_sum_subarray(arr, k):
    max_sum = window_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum

test_case_1 = [-2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(test_case_1, k))