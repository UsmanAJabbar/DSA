def invertTree(root):
    def helper(root):
        if not root: return

        root.left, root.right = root.right, root.left
        helper(root.left)
        helper(root.right)

        return root

    helper(root)
    return root
