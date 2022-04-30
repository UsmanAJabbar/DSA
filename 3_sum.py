from collections import defaultdict
from math import ceil

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
    results = []

    element_count = defaultdict(int)
    while nums:
        v = nums.pop()
        element_count[v] += 1

    keys = sorted(element_count.keys())

    for l in keys:
        if l > 0:
            break
        elif l == 0:
            if element_count[0] >= 3:
                results.append([0, 0, 0])
        else:
            search_lower_bound = ceil(abs(l) / 2)
            search_upper_bound = 2 * abs(l)

            for idx in range(1, len(keys) + 1):
                r = keys[-idx]
                if   r > search_upper_bound: continue
                elif r < search_lower_bound: break
                else:
                    m = 0 - (l + r)
                    if m in element_count:
                        r_count = element_count[r]
                        m_count = element_count[m]
                        if (
                            (l == m and m_count >= 2) or
                            (m == r and r_count >= 2) or
                            (l != m and m != r)
                        ):
                            results.append([l, m, r])

    return results
