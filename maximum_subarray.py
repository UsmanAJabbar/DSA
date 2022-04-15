def maximum_subarray(nums):
    subarray_max = float('-inf')
    global_max = nums[0]

    for curr_num in nums:
        subarray_max = max(
            curr_num,
            subarray_max + curr_num
        )

        global_max = max(global_max, subarray_max)
    
    return global_max
