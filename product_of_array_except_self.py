def product_array_except_self(nums):
    """
    ----------------------------
    PRODUCT OF ARRAY EXCEPT SELF
    ----------------------------
    Given an integer array nums, return an array
    answer such that answer[i] is equal to the
    product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is
    guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n)
    time and without using the division operation.

    Args:
        nums (list): list of numbers

    Source: https://leetcode.com/problems/product-of-array-except-self/
    """
    # Plan
    # The goal here is to complete the problem that runs in O(n)

    # Here's my understanding after getting the answers from elsewhere
    # Let's say we have [ 2, 4, {10}, 2, 7 ]
    # Let's say we're currently on the 10 above. What if we could have
    # the total of everything on the right right next to the 10
    # and the total product of everything on the left left of the 10.
    # We could multiply the two and then get the final answer
    # that way super easily

    # For this solution, we're gonna use two arrays that get the total product
    # from the prespectives on the right end and left end of the array
    l_product, r_product = [], []

    running_product = 1
    for i in range(len(nums)):
        running_product *= nums[i]
        l_product.append(running_product)

    running_product = 1
    for j in range(len(nums) -1, -1, -1):
        running_product *= nums[j]
        r_product.append(running_product)

    r_product = list(reversed(r_product))

    output = []
    for i in range(len(nums)):
        x = (
            l_product[i - 1]
            if i - 1 != -1
            else 1
        )
        y = (
            r_product[i + 1]
            if i + 1 < len(nums)
            else 1
        )
        output.append(
            x * y
        )

    return output
