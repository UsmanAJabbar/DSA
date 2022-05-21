def word_search(board, word) -> bool:
    visited = set()

    board_height, board_length = len(board), len(board[0])

    def backtrack(idx: int, x: int, y: int) -> bool:
        if (
            x < 0 or x >= board_length or
            y < 0 or y >= board_height or
            (x, y) in visited or
            board[y][x] != word[idx]
        ): return False

        visited.add((x, y))
        res = (
            idx + 1 == len(word) or
            backtrack(idx + 1, x + 1, y) or
            backtrack(idx + 1, x - 1, y) or
            backtrack(idx + 1, x, y + 1) or
            backtrack(idx + 1, x, y - 1)
        )
        visited.remove((x, y))

        return res

    for y in range(board_height):
        for x in range(board_length):
            if board[y][x] == word[0]:
                if backtrack(0, x, y):
                    return True

    return False
