def max_sum_subarray(arr, k):
    max_sum = sum(arr[:k])
    window_sum = max_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum
    
my_array = [1, 2, 3, 4, 5, 2, 1, 7, 1]
print(max_sum_subarray(my_array, 2)) # output 9 because the largest combination of 2 numbers right next to each other is 4 and 5
