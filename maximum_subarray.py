def max_subarray(nums):
    subarray_sum = 0
    global_max = nums[0]

    for n in nums:
        subarray_sum += n

        if subarray_sum > global_max:
            global_max = subarray_sum

        if subarray_sum < 0:
            subarray_sum = 0

    return global_max

print(
    max_subarray(
        [-2,1,-3,4,-1,2,1,-5,4]
    )
)