def find_max(arr, left, right, text):
    if left == right:
        return arr[left]

    print(text)
    print(arr[left:right + 1])
    

    mid = (left + right) // 2
    left_max = find_max(arr, left, mid, 'left_max')
    right_max = find_max(arr, mid + 1, right, 'right_max')

    return max(left_max, right_max)


my_array = [3, 2, 5, 6, 10]

print(find_max(my_array, 0, len(my_array) - 1, 'start'))

