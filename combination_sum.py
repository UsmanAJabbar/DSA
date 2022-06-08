def combination_sum_naive(candidates: list, target: int) -> list:
    unique_combinations = set()
    candidates.sort()

    def backtrack(target: int, path: list):
        if target  < 0: return
        if target == 0:
            unique_combinations.add(
                tuple(sorted(path))
            )

        for opt in candidates:
            path.append(opt)
            backtrack(target - opt, path)
            path.pop()


    current_path = []
    backtrack(target, current_path)

    return unique_combinations.values()


def combination_sum_knapsack(candidates: list, target: int) -> list:
    result = []
    candidates.sort()

    def backtrack(opt_idx: int, path: list, total: int) -> None:
        if total > target or opt_idx >= len(candidates):
            return

        if total == target:
            result.append(path[:])
            return

        current_candidate = candidates[opt_idx]

        path.append(current_candidate)
        backtrack(opt_idx, path, total + current_candidate)
        path.pop()
        backtrack(opt_idx + 1, path, total)

    backtrack(0, [], 0)
    return result


def combination_sum_knapsack_rv(candidates: list, target: int) -> list:
    result = []
    candidates.sort()

    def backtrack(opt_idx: int, path: list, target: int) -> None:
        if target < 0 or opt_idx >= len(candidates):
            return

        if target == 0:
            result.append(path[:])
            return

        current_candidate = candidates[opt_idx]

        path.append(current_candidate)
        backtrack(opt_idx, path, target - current_candidate)
        path.pop()
        backtrack(opt_idx + 1, path, target)

    backtrack(0, [], target)
    return result


inputs = [
    [100,200,4,12],
    400
]

reverse = combination_sum_knapsack_rv(*inputs)
normal = combination_sum_knapsack(*inputs)

print('Self test', reverse == normal)
