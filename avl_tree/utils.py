def get_height(node):
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    return 0 if not node else get_height(node.left) - get_height(node.right)
