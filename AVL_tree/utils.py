def get_height(node):
    return 0 if not node else node.height

def get_balance(node):
    return 0 if not node else get_height(node.left) - get_height(node.right)
