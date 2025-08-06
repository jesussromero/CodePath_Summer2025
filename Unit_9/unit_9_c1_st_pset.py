'''
Problem 1: Merging Cookie Orders

You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree 
represents the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough 
of each type of cookie for both orders together.

Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders,
 imagine that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not. 
 If two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the not None node will be used 
 as the node of the new tree.

Start the merging process from the root of both orders.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you 
believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    pass

Example Usage:

Example 'order1' and 'order2' trees and their merged result

"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

Example Usage:

[3, 4, 5, 5, 4, None, 7]
Explanation:
Merged Tree:
     3
    /  \      
  4     5  
 / \      ''
5   4      7

'''
from collections import deque

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

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

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right
#U: Idea is to add the values of both trees at the same index/root and return the root of that tree
#M: Traversal sub-problem
#P: 
def merge_orders(order1, order2):
    #1. Traverse through both trees and return a list with all of the values
    #2. Add both lists by index
    #3. Build the tree based on the new list
    #4. Return root of said tree

    modified_root = order1

    def helper(o1, o2):
        if not o1 and not o2:
            return
        # base case: if only order1 node exists
        if not o2:
            return o1
        # base case: if only order2 node exists
        if not o1:
            return o2
        
        o1.val = o1.val + o2.val
        o1.left = helper(o1.left, o2.left)
        o1.right = helper(o1.right, o2.right)

        return o1

    helper(order1, order2)

    return modified_root




    
def traversal(root, first_tree):
    if root is None:
       
       return root
    
    first_tree.append(root.val)

    traversal(root.left, first_tree)
    traversal(root.right, first_tree)

    return first_tree


    #result = []
    #first_tree = []
    #second_tree = []




cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

tree = []
print(traversal(order2, tree))

print_tree(merge_orders(order1, order2))