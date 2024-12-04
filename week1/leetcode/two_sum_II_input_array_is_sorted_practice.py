# leetcode.com
# 167. Two Sum II - Input Array Is Sorted

def two_pointers(arr, target):
    left_pointer = 0
    right_pointer = len(arr) - 1

    target_not_found = True

    while target_not_found:
        if arr[left_pointer] + arr[right_pointer] == target:
            target_not_found = False
            return [left_pointer, right_pointer]
        elif arr[left_pointer] + arr[right_pointer] < target:
            left_pointer += 1
        else:
            right_pointer -= 1

    return two_pointers(numbers, target)


my_array = [7,8,5,1,3]
target = 9

print(two_pointers(my_array, target))
