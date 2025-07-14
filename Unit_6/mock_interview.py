'''
Write a function to find the intersection of 2 singly linked lists. Return the node at which the 
linked lists intersect. If the 2 lists have no intersection, return None.
For example, in the below screenshot from Leetcode, the 2 lists intersect at c1 so your 
function should return a reference to c1.
'''
#U: We are given two linked lists as inputs. We are supposed to return the point at which both point
#   to the same memory address, if it doesn't exit, return None. If it does exit, return the node at
#   which the intersection occurs
#MP: Iterate once over the first linked list. Use a set to keep track of the values. Then, Iterate again
#   over the second linked list, and if there is a same value in the set, then that's when the intersection
#   happens
