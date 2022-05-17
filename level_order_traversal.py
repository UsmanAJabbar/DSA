def level_order_traversal(root) -> list:
    collection = []

    if not root: return collection

    def helper(root, level) -> list:
        nonlocal collection
        if not root: return

        # The idea here is to keep track of the levels
        # Since we have the level that also acts as idxs, we can
        # append our new value to that index

        # On the first run, our idx would most likely not exist (esp when moving left)
        # However, when the call stack comes back up and then moves onto the right node
        # we could now have an idx available in collection that we could append to
        if len(collection) <= level:
            collection += [[root.val]]
        else:
            collection[level] += [root.val]

        helper(root.left, level + 1)
        helper(root.right, level + 1)

    helper(root, 0)
    return collection
