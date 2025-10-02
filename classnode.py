class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def level_order_rec(root, level, res):
    """Recursive helper function to perform level-order traversal."""
    
    if root is None:
        return

    
    if len(res) <= level:
        res.append([])

   
    res[level].append(root.data)

   
    level_order_rec(root.left, level + 1, res)
    level_order_rec(root.right, level + 1, res)

def level_order(root):
    """Main function to initiate the recursive level-order traversal."""
    res = []
    level_order_rec(root, 0, res)
    return res

if __name__ == '__main__':
    # Tree Structure:
    #         5
    #        / \
    #      12   13
    #     /  \   \
    #    7   14   2
    #   / \  / \ / \
    # 17 23 27 3 8 11
    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(7)
    root.left.right = Node(14)
    root.right.right = Node(2)
    root.left.left.left = Node(17)
    root.left.left.right = Node(23)
    root.left.right.left = Node(27)
    root.left.right.right = Node(3)
    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    result = level_order(root)

    print("Level-Order Traversal (Recursive):")
    for level in result:
        print(f"[{', '.join(map(str, level))}] ", end='')
    print() # For a final newline