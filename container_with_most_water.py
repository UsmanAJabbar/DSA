def container_with_most_water(height: list) -> int:
    l, r = 0, len(height) - 1
    
    max_container = 0
    while l < r:
        max_container = max(
            max_container,
            min(height[l], height[r]) * (r - l)
        )
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return max_container