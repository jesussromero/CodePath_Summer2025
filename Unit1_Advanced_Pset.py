#Solving advanced psets for fun

from typing import List
'''
1) Write a function linear_search() to help Winnie the Pooh locate his lost items.
The function accepts a list items and a target value as parameters.
The function should return the first index of target in items,
and -1 if target is not in the lst.
Do not use any built-in functions.
'''

'''
Input: List of elements
Output: index of target
Strat: iterate over every single element in the list and return its index
'''

def linear_search(lst, target):
    for i in range(len(lst)):
        if target == lst[i]:
            return print(i)
    return print(-1) #Works

'''
2) Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around!

Given a list of strings operations containing a list of operations,
return the final value of tigger after performing all the operations.
'''

'''
input: list of operations
output: an integer with the final value (starting of 1)
strat: iterate over the list and use if conditions
'''

def final_value_after_operations(operations):
    value = 1
    if len(operations) == 0:
        return value
    
    for operation in operations:
        if (operation == 'bouncy') or (operation == 'flouncy'):
            value += 1
        elif (operation == 'trouncy') or (operation == 'pouncy'):
            value -= 1
    return print(value) #works

'''
3) Problem 3: T-I-Double Guh-Er II
T-I-Double Guh-Er: That spells Tigger! 
Write a function tiggerfy() that accepts a string word and returns a new string 
that removes any substrings t, i, gg, and er from word. 
The function should be case insensitive
'''
'''
Input: word
Output: Word with the letters t, i, gg and er removed
Strat: Iterate over the letters in the word and look for the ones listed
'''
 
def tiggerfy(word):
    word = word.lower()
    result = ''
    i = 0
    # Using a while loop to control how many chars to skip
    while i < len(word):
        if word[i] in ['t', 'i']:
            i += 1
            continue
        # We check from the word's index [i to i+2), this wouldn't cause an Out of Range error too
        elif word[i:i+2] == 'gg':
            i += 2
            continue
        elif word[i:i+2] == 'er':
            i += 2
            continue
        else:
            result += word[i]
            i += 1
    return print(result) # works

'''
Given an array nums with n integers,
write a function non_decreasing() that checks if nums could become non-decreasing
by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
such that (0 <= i <= n - 2).

nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)

nums = [2, 3, 1]
nums = [1, 2, 1, 4]

input: list of numbers
output: a boolean that determines whether the list is in ascending order and if not, if modifying
one value is enough to make it ascending
strat: look for the highest value number and check if the following elements meet the condition.
'''
def non_decreasing(nums):
    max = 0
    state = True
    previous = nums[0]
    for number in nums:
        if number > max:
            max == number
            continue
        if previous > number:
            return False
        