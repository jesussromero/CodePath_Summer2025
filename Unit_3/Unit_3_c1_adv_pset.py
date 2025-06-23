from collections import deque
'''
Problem 1: Arrange Guest Arrival Order

You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status.
The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Return the lexicographically smallest possible string guest_order that meets the conditions.

def arrange_guest_arrival_order(arrival_pattern):
    pass

Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  
Example Output:
123549876
II -> ascending order

1 2 3 4 5 6 7 8 9
'''

def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    result = []
    
    for i in range(len(arrival_pattern) + 1):
        # Push the next number (1-indexed)
        stack.append(i + 1)
        print(stack)
        # If it's the end or the current char is 'I', flush the stack
        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                result.append(stack.pop())
        print(result)
    
    return ''.join(str(num) for num in result)


'''
Problem 2: Reveal Attendee List in Order
You are organizing an event where attendees have unique registration numbers.
These numbers are provided in the list attendees.
You need to arrange the attendees in a way that, when their registration numbers are revealed one by one,
the numbers appear in increasing order.

The process of revealing the attendee list follows these steps repeatedly until all registration numbers are revealed:

Take the top registration number from the list, reveal it, and remove it from the list.
If there are still registration numbers in the list, take the next top registration number and move it to the bottom of the list.
If there are still unrevealed registration numbers, go back to step 1. Otherwise, stop.
Return an ordering of the registration numbers that would reveal the attendees in increasing order.

def reveal_attendee_list_in_order(attendees):
    pass

Example Usage:

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  

Example Output:

[2,13,3,11,5,17,7]
[1,1000]
'''




