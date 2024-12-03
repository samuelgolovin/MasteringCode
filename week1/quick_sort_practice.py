def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

my_array = [3, 6, 21, 87, 5, 34, 14, 2, 8, 43]
print(quick_sort(my_array)) # outputs sorted array
