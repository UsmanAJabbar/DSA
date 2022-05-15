def max_depth_binary_tree(root) -> int:
    def dfs(root, depth):
        if not root: return depth
        return max(
            dfs(root.left, depth + 1),
            dfs(root.right, depth + 1)
        )
    return dfs(root, 0)
