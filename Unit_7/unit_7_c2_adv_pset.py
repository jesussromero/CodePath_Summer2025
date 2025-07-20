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