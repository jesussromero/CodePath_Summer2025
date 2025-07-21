'''
Problem 1: Finding the Perfect Cruise

It's vacation time! Given an integer vacation_length and a list of integers
cruise_lengths sorted in ascending order, use binary search to return True if 
there is a cruise length that matches vacation_length and False otherwise.

def find_cruise_length(cruise_lengths, vacation_length):
    pass

Example Usage:

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

Example Output:

True
False

'''
def find_cruise_length(number_list, target):
    #1. Edge cases: length of list is 1, empty
    if len(number_list) == 0:
        return False
    elif len(number_list) == 1 and number_list[0] == target:
        return True
    #2. Set left, right pointers and start while loop
    left = 0
    right = len(number_list) - 1
    #3. Start of the algorithm 
    while left <= right:
        middle = (left + right)//2
        if number_list[middle] == target:
            return True
        elif target > number_list[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return False #Time, Space complixities: O(log_2(n)), O(1)

'''
Problem 2: Booking the Perfect Cruise Cabin

As part of your cruise planning, you have a list of available cabins sorted in 
ascending order by their deck level. Given the list of available cabins represented 
by deck level, cabins, and an integer preferred_deck, write a recursive function 
find_cabin_index() that returns the index of preferred_deck. If a cabin with your 
preferred_deck does not exist in cabins, return the index where it would be if it 
were added to the list to maintain the sorted order.

Your algorithm must have O(log n) time complexity.

def find_cabin_index(cabins, preferred_deck):
    pass

Example Usage:

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))

Example Output:

2
1
4

'''

def find_cabin_index(cabins, preferred_deck):
    def recursive_helper(left, right):
        if left > right:
            return left
        middle = (left + right) // 2
        if preferred_deck == cabins[middle]:
            return middle
        elif preferred_deck > cabins[middle]:
            return recursive_helper(middle + 1, right)
        else:
            return recursive_helper(left, middle - 1)
    return recursive_helper(0, len(cabins) - 1)


#print(find_cabin_index([1, 3, 5, 6], 5))
#print(find_cabin_index([1, 3, 5, 6], 2))
#print(find_cabin_index([1, 3, 5, 6], 7))

'''
Problem 3: Count Checked In Passengers

As a cruise ship worker, you're in charge of tracking how many passengers have checked 
in to their rooms thus far. You are given a list of rooms where passengers are either 
checked in (represented by a 1) or not checked in (represented by a 0). The list is sorted, 
so all the 0s appear before any 1s.

Write a function count_checked_in_passengers() that efficiently counts and returns the total 
number of checked-in passengers (1s) in the list in O(log n) time.

def count_checked_in_passengers(rooms):
    pass

Example Usage:

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))

Example Output:

4
1
0
'''
def count_checked_in_passengers(rooms):
    #1. Check for edge cases: rooms is empty, only 1 element present
    if(len(rooms) == 0):
        return -1
    elif(len(rooms) == 1) and (rooms[0] == 1):
        return 1
    elif(len(rooms) == 1) and (rooms[0] == 0):
        return 0
    elif(rooms[len(rooms) - 1]) == 0:
        return 0
    #2. Start the binary search following this algorithm:
    #2. Set left, right pointers and start while loop
    left = 0
    right = len(rooms) - 1
    earliest = 0
    #3. Start of the algorithm 
    while left <= right:
        middle = (left + right)//2
        if rooms[middle] == 0:
            left = middle + 1
        elif rooms[middle] == 1:
            if earliest == 0:
                right = middle - 1
                earliest = right
    return (len(rooms)-earliest-1)
        
    #2.1 Check for the earliest appeareance of 1 in the list
    #3 Return the number of checked in people len(room) - earliest 1 

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

#print(count_checked_in_passengers(rooms1)) 
#print(count_checked_in_passengers(rooms2))
#print(count_checked_in_passengers(rooms3))