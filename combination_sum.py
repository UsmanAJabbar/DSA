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
