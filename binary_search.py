#!/usr/bin/python3

def binary_search(array, target):
    first_index = 0
    last_index = len(array) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if array[mid_index] == target:
            return True 
        elif array[mid_index] > target:
            last_index = mid_index - 1
        else:
            first_index = mid_index + 1

    return False


def binary_search_recursive(array, target):
    if not array: return False

    first_idx, last_idx = 0, len(array) - 1
    mid_idx = (first_idx + last_idx) // 2

    if array[mid_idx] == target: return True

    array = (
        array[:mid_idx]             # Split the array in half and get the first half
        if target < array[mid_idx]
        else array[mid_idx + 1:]    # Split the array in half and get the second half
    )

    return binary_search_recursive(array, target)


array = [2, 17, 21, 42, 94, 1102, 1234, 1255, 2245]
targets = [
    42,
    65
]

for target in targets:
    print(
        binary_search_recursive(array, target)
    )
