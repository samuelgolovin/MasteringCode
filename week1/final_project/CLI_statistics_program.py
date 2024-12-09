# CLI program that calculates and displays statistics
# (mean, median, and mode) from a list of numbers entered by the user.


# functions
def check_if_number(input_value):
    try:
        int_value = int(input_value)
        print(f"Input is an integer: {int_value}")
        return int_value
    except ValueError:
        try:
            float_value = float(input_value)
            print(f"Input is a float: {float_value}")
            return float_value
        except ValueError:
            return False

def find_statistics(arr):
    print("the given numbers are: ")
    print(arr)
    print()
    print()
    
    # find the mean
    size = len(arr)
    arr_sum = 0
    for x in arr:
        arr_sum += x
    mean = arr_sum / size

    # find the median
    sorted_arr = arr
    sorted_arr.sort()
    print(sorted_arr)
    if len(arr) > 1:
        if size % 2 != 0:
            median = sorted_arr[(size // 2) + 1]
        else:
            print(2 // 2)
            median = (sorted_arr[(size // 2) - 1] + sorted_arr[(size // 2)]) / 2
    else:
        median = arr[0]

    # find the mode
    if size > 1:
        most_common_nums = []
        max_nums = 0
        for x in arr:
            if arr.count(x) > max_nums:
                max_nums = arr.count(x)
                most_common_nums.clear()
                most_common_nums.append(x)
            elif arr.count(x) == max_nums and x not in most_common_nums:
                max_nums = arr.count(x)
                most_common_nums.append(x)

        mode = most_common_nums
    else:
        mode = arr[0]
        

    # find the min, max, range
    arr_min = min(arr)
    arr_max = max(arr)
    arr_range = arr_max - arr_min


    return [mean, median, mode, size, sorted_arr, arr_sum, arr_range, arr_min, arr_max]
        

# array of input numbers
array = []

print("This program takes in numbers, add them to an array, and then gives the mean, \
median, and mode of those numbers.")

while True:
    number = input("Add a number to array, 'd' when done, 'e' to exit: ")

    check = check_if_number(number)
    if check:
        array.append(check)
        continue
    elif check == False:
        if number == 'd' or number == 'D':
            if len(array) > 0:
                findings = find_statistics(array)
            else:
                print("No numbers were given. Try again.")
                continue
        elif number == 'e' or number == 'E':
            break
        else:
            print("Try again.")
            continue

    print("Mean: ", findings[0])
    print("Median: ", findings[1])
    print("Mode: ", findings[2])
    print("Elements in list: ", findings[3])
    print("Sorted list: ", findings[4])
    print("Sum: ", findings[5])
    print("Range: ", findings[6])
    print("Min: ", findings[7])
    print("Max: ", findings[8])
        
