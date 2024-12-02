def max_sum_subarray(arr, k):
    max_sum = sum(arr[:k])
    window_sum = max_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum
