'''
Problem 1: Counting Treasure
Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

def total_treasure(treasure_map):
    pass
Example Usage:

Example Output:

15
50
'''

import math


def total_treasures(treasure_map):
    return sum(treasure_map.values())

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

#print(total_treasures(treasure_map1)) 
#print(total_treasures(treasure_map2)) 


'''
Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.


Example Usage:


Example Output:

True
False
'''

def can_trust_message(message):
    # get rid of white space
    message = message.replace(" ", "")
    # count every letter, check if length is 26
    x = set()
    for letter in message:
        x.add(letter)

    return len(x) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

'''
Problem 3: Find All Duplicate Treasure Chests in an Array
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

def find_duplicate_chests(chests):
    pass
Example Usage:

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
Example Output:

[2, 3]
[1]
[]
'''

def find_duplicate_chests(chests):
    my_dict = {}
    ans = []
    for num in chests:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += 1
            if my_dict[num] == 2:
                ans.append(num)
    return ans
    
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

'''
Problem 4: Booby Trap
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

Example Output:

True
Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

False
Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice versa. It is impos
'''


def is_balanced(code):
    # if it's possible to remove one letter so that the frequency of all remaining letters is equal
    # use dict 
    my_dict = {}
    for letter in code:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1
    # only 1 letter can have 1 more freq 
    x = set()
    for key, value in my_dict.items():
        x.add(value)
    
    result = list(x)

    if len(result) == 2:
        if abs(result[0] - result[1]) == 1:
            return True
    else:
        return False


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 



'''
Problem 5: Overflowing With Gold
Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on their ship.

Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, return the indices of the two locations whose gold amounts add up to the target.

Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

Example Output:

[0, 1]
[1, 2]
[0, 1]
'''

def find_treasure_indices(gold_amounts, target):
    dict = {}
    for i, gold in enumerate(gold_amounts):
        if target - gold in dict:
            return [dict[target - gold], i]
        dict[gold] = i 
    return [-1,-1]

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

 


'''
Problem 6: Organize the Pirate Crew
Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.

You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.

Return a list of groups such that each pirate i is in a group of size group_sizes[i].

Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

def organize_pirate_crew(group_sizes):
    pass
Example Usage:

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
Example Output:

[[5], [0, 1, 2], [3, 4, 6]]
[[1], [0, 5], [2, 3, 4]]
'''

'''
Problem 7: Minimum Number of Steps to Match Treasure Maps
Captain Blackbeard has two treasure maps represented by two strings of the same length map1 and map2. In one step, you can choose any character of map2 and replace it with another character.

Return the minimum number of steps to make map2 an anagram of map1.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

def min_steps_to_match_maps(map1, map2):
    pass
Example Usage:

map1_1 = "bab"
map2_1 = "aba"
map1_2 = "treasure"
map2_2 = "huntgold"
map1_3 = "anagram"
map2_3 = "mangaar"

print(min_steps_to_match_maps(map1_1, map2_1))
print(min_steps_to_match_maps(map1_2, map2_2))
print(min_steps_to_match_maps(map1_3, map2_3))
Example Output:

1
6
0
'''

'''
Problem 8: Counting Pirates' Action Minutes
Captain Dread is keeping track of the crew's activities using a log. The logs are represented by a 2D integer array logs where each logs[i] = [pirateID, time] indicates that the pirate with pirateID performed an action at the minute time.

Multiple pirates can perform actions simultaneously, and a single pirate can perform multiple actions in the same minute.

The pirate action minutes (PAM) for a given pirate is defined as the number of unique minutes in which the pirate performed an action. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of pirates whose PAM equals j.

Return the array answer as described above.

def counting_pirates_action_minutes(logs, k):
    pass
Example Usage:

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))
Example Output:

[0, 2, 0, 0, 0]
[1, 1, 0, 0]
'''