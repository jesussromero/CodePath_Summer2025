# Mock Interview Problem
'''
Problem 1: Greatest Node
Write a function find_max() that takes in the head of a linked list and returns the maximum
value in the linked list. You can assume the linked list will contain only numeric values.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

Example Usage:

head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))
Expected Output:

8
8
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    # 1. Store the first value, and compare to the rest
    max_val = head.value
    current = head
    while current:
        if current.value > max_val:
            max_val = current.value
        current = current.next
    return max_val





'''
Problem 2: Remove Tail

The following code incorrectly implements the function remove_tail(). When correctly implemented, remove_tail() accepts the head of a singly linked list and removes the last node (the tail) in the list. The function should return the head of the modified list.

Step 1: Copy this code into Replit.

Step 2: Create your own test cases to run the code against. Use print statements, print_linked_list(), and the stack trace to identify and fix any bugs so that the function correctly removes the last node from the list.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next: 
        current = current.next

    current.next = None 
    return head

Example Usage:

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

Expected Output:

Isabelle -> Alfonso

'''
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

'''
Problem 3: Delete Duplicates in a Linked List
Given the head of a sorted linked list, delete all elements that occur more than once in the 
list (not just the duplicates). The resulting list should maintain sorted order. Return the head 
of the linked list.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    pass
Example Usage:

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
Example Output:

1 -> 2 -> 4 -> 5
'''
# {1,2,3,4,5}
# {3}
# 1 -> 2 -> 3 -> 3 -> 4 ->5
#      S              F 
# Save the first node after the duplicates (4)
# Keep track of the node before the duplicate 
# Set it to the saved node
def delete_dupes(head):
    my_set = set()
    dupes = set()
    current = head
    # Works
    while current:
        if current.value in my_set:
            dupes.add(current.value)
        else:
            my_set.add(current.value)
        current = current.next

    # Second pass: remove nodes with duplicate values
    dummy = Node(0)  # Add dummy to handle edge cases cleanly
    dummy.next = head
    slow = dummy
    fast = head

    while fast:
        if fast.value in dupes:
            fast = fast.next  # skip the duplicate
        else:
            slow.next = fast
            slow = fast
            fast = fast.next

    slow.next = None  # end the list
    return dummy.next
    

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

#head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(4))))))
# Linked List: 1 -> 2 
#print_linked_list(delete_dupes(head))