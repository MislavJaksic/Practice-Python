# Maximum Subarray Problem is a famous problem
# The solution is called Kadane's algorithm

def max_sequence(arr):  # brute force solution
    maximum = 0
    for window_size in range(1, len(arr)+1):
        for offset in range(len(arr)+1-window_size):
            maximum = max(maximum, sum(arr[offset:offset+window_size]))
    return maximum


def max_sequence_on(arr):  # kadane's algorithm
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in arr:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum