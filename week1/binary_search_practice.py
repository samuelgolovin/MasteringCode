def binary_search(arr, target):
    def search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)

    return search(0, len(arr) - 1)

my_array = [16, 23, 31, 42, 56, 65, 75, 84, 93]
print(binary_search(my_array, 31)) # output 2 since 31 is the third element in my_array
