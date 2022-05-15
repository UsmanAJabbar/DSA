def compare_binary_tree(p, q) -> bool:
    if (
        (not p and q) or
        (not q and p) or
        (
            p and q and
            p.val != q.val
        )
    ): return False

    if not p and not q: return True

    return (
        compare_binary_tree(p.left, q.left) and
        compare_binary_tree(p.right, q.right)
    )
