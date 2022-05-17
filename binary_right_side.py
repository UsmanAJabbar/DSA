def binary_tree_right_side_view_dfs(root) -> list:
    """
    The initial plan here is to always move right
    If we ever come across a NULL right, move left until we find another right

    As long as rights exist, we will continue to append our values to the list
    """
    collection = []

    if not root: return collection

    def helper(node, level: int):
        nonlocal collection
        if not node: return

        collection += [node.val]

        if len(collection) == level:
            collection.append(node.val)
        helper(node.right, level + 1)
        helper(node.left, level + 1)

    helper(root, 0)
    return collection


def binary_tree_right_side_view_bfs(root) -> list:
    collection = []

    if not root: return collection

    queue = [root]

    while queue:
        collection.append(queue[-1].val)
        queue_children = []

        for node in queue:
            if node.left:  queue_children.append(node.left)
            if node.right: queue_children.append(node.right)

        queue = queue_children

    return collection
