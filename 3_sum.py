def three_sum_brute_force(nums: list) -> list:
    nums.sort()
    rec = set()
    res = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0 and (nums[i], nums[j], nums[k]) not in rec:
                    rec.add((nums[i], nums[j], nums[k]))
                    res.append([nums[i], nums[j], nums[k]])

    return res


def three_sum(nums: list) -> list:
    if len(nums) < 3: return []

    nums.sort()
    rec = set()
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        base = nums[i]
        start, end = i + 1, len(nums) - 1
        while start < end:
            total = base + nums[start] + nums[end]
            if total > 0:
                end -= 1
            else:
                if total == 0 and (base, nums[start], nums[end]) not in rec:
                    rec.add((base, nums[start], nums[end]))
                    res.append([
                        base, nums[start], nums[end]
                    ])
                start += 1

    return res
