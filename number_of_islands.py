def numIslands(grid: list) -> int:
    if not grid or not grid[0]: return 0

    ISLAND = '1'
    WATER = '0'

    number_of_islands = 0
    grid_height, grid_length = len(grid), len(grid[0])

    def backtrack(x, y):
        if (
            x < 0 or x >= grid_length or
            y < 0 or y >= grid_height or
            grid[y][x] is not ISLAND
        ): return

        grid[y][x] = WATER

        backtrack(x + 1, y)
        backtrack(x - 1, y)
        backtrack(x, y + 1)
        backtrack(x, y - 1)

    for y in range(grid_height):
        for x in range(grid_length):
            if grid[y][x] is ISLAND:
                backtrack(x, y)
                number_of_islands += 1

    return number_of_islands
