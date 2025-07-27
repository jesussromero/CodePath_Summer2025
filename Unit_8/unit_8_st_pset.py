'''
Problem 1: Grafting Apples

You are grafting different varieties of apple onto the same root tree can produce 
many different varieties of apples! Given the following TreeNode class, create the 
binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

             Trunk
          /         \
      Mcintosh   Granny Smith
      /     \       /     \
    Fuji   Opal   Crab   Gala

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")

Example Usage:

# Using print_tree() included at the top of this page
print_tree(root)

Example Output:

['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']

'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque
def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")

print_tree(root)