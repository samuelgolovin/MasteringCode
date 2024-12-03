def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            print(arr[left], arr[right])
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1

my_array = [1, 2, 3, 4, 5]
two_sum_sorted(my_array, 4) # output 1 3 because those add up to 4
