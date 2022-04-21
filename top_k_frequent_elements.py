def top_k_frequent_elements(nums: list, k: int) -> list:

    def element_counter(arr) -> dict:
        count = {}
        for x in arr:
            count[x] = count.get(x, 0) + 1
        return count

    bucket = [
        [] for _ in range(len(nums) + 1)
    ]

    element_count = element_counter(nums)

    for element in element_count:
        bucket[
            element_count[element]
        ].append(element)

    result = []
    idx = len(bucket) - 1
    while k > 0:
        if bucket[idx]:
            result += bucket[idx]
            k -= len(bucket[idx])
        idx -= 1

    return result
