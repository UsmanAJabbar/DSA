#!/usr/bin/env python3
"""Search 2D Matrix"""


"""
PLAN:
    - We could easily look for the value in the arrays
    with a nested for loop
    - To make it more efficient, we're gonna loop through
    the array and check whether the target would most likely
    land in the current array.
    - If we found the array where the target may be, we could
    simply do a binary search and look for the target in there
    - Return True/False accordingly
"""


def binary_search(array, target):
    """Helper function"""
    upper_bound, lower_bound = 0, len(array) - 1

    while upper_bound <= lower_bound:
        mid_idx = (upper_bound + lower_bound) // 2
        if array[mid_idx] == target:
            return True
        elif array[mid_idx] > target:
            lower_bound = mid_idx - 1
        else:
            upper_bound = mid_idx + 1

    return False


def search_2d_matrix(matrix, target):
    """
    ----------------
    Search 2D Matrix
    ----------------
    Write an efficient algorithm that searches for a value
    target in an m x n integer matrix @matrix.

    This 2D matrix has the following properties:
        * Integers in each row are sorted from left to right.
        * The first integer of each row is greater than the
          last integer of the previous row.
    """
    for arr in matrix:
        # Check if our target appears between the first and last values in our arr
        if arr[0] <= target <= arr[-1]:
            return binary_search(arr, target)
        # If we're past an arr, break and return None immediately.
        elif arr[0] > target:
            break

    return False