'''
Problem 1: Counting the Layers of a Sandwich
You're working at a deli, and need to count the layers of a sandwich to make sure you made 
the order correctly. Each layer is represented by a nested list. Given a list of lists sandwich 
where each list [] represents a sandwich layer, write a recursive function count_layers() that 
returns the total number of sandwich layers.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def count_layers(sandwich):
    pass
Example Usage:

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))
Example Output:

4
5
'''
def count_layers(sandwich):
    #1. Check for edge cases like list is empty or there is only one element
    if len(sandwich) == 0:
        return 0
    elif len(sandwich) == 1:
        return 1
    #2. Use recursion to iterate over all layers and increase count per layer traversed
    print(sandwich[1])
    return count_layers(sandwich[1]) + 1


#sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
#sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
#print(len(sandwich1), len(sandwich2))
#print(count_layers(sandwich1))
#print(count_layers(sandwich2)) # Time, Space complexity: O(n), O(1)

'''
Problem 2: Reversing Deli Orders
The deli counter is busy, and orders have piled up. To serve the last customer first, 
you need to reverse the order of the deli orders. Given a string orders where each individual 
order is separated by a single space, write a recursive function reverse_orders() that returns 
a new string with the orders reversed.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def reverse_orders(orders):
    pass
Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))
Example Output:

Coffee Sandwich Bagel
'''

# Time complexity: O(n)
# Space complexity: O(n)
def reverse_orders(orders):
    order_list = orders.split()
    return recurse_reverse_orders(order_list)

# recurse_reverse_orders(["Coffee", "Sandiwch"])
def recurse_reverse_orders(lst):
    if len(lst) == 1:
        return lst[0]
    # return last list element, and recurse on a smaller list
    return lst[-1] + " " + recurse_reverse_orders(lst[0:-1])

    
#print(reverse_orders("Bagel Sandwich Coffee"))

'''
Problem 3: Sharing the Coffee
The deli staff is in desperate need of caffeine to keep them going through their shift 
and has decided to divide the coffee supply equally among themselves. Each batch of coffee 
is stored in containers of different sizes. Write a recursive function can_split_coffee() 
that accepts a list of integers coffee representing the volume of each batch of coffee and 
returns True if the coffee can be split evenly by volume among n staff and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def can_split_coffee(coffee, n):
pass
Example Usage:

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
Example Output:

True
False
'''
def can_split_coffee(coffee, n):
    #1. The formula would be: coffee % n = 0 if it can be evenly districuted, else it can't
    #2. For algo design purposes, this will be done iteratively by checking the condition in each index
    for volume in coffee:
        if volume%n != 0:
            return False
    return True

#print(can_split_coffee([4, 4, 8], 2))
#print(can_split_coffee([5, 10, 15], 4))

'''
Problem 4: Super Sandwich
A regular at the deli has requested a new order made by merging two different sandwiches on 
the menu together. Given the heads of two linked lists sandwich_a and sandwich_b where each 
node in the lists contains a spell segment, write a recursive function merge_orders() that 
merges the two sandwiches together in the pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

Return the head of the merged sandwich.

Evaluate the time and space complexity of your solution. Define your variables and provide 
a rationale for why you believe your solution has the stated time and space complexity.'''

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

#Example Usage:

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

#Example Output:
'''
Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
Bacon -> Bread -> Lettuce -> Tomato
'''


# example input: Bacon -> Lettuce -> Tomato
#                Turkey -> Cheese -> Mayo
#                Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
def merge_orders(sandwich_a, sandwich_b):
    a_ptr = sandwich_a
    b_ptr = sandwich_b
    c = sandwich_a
    flag_a = 0
    flag_b = 0
    while a_ptr and b_ptr:
        if flag_b == 0:
            c.next = b_ptr
            c = c.next
            flag_b = 1
            flag_a = 0
            b_ptr = b_ptr.next
        elif flag_a == 0:
            c.next = a_ptr
            c = c.next
            flag_a = 1
            flag_b = 0 
            a_ptr = a_ptr.next

    return c
    
print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))