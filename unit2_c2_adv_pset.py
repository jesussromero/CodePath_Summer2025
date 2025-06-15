from collections import Counter

# Problem 1: Balanced Art Collection
# As the curator of an art gallery, you are organizing a new exhibition.
# You must ensure the collection of art pieces are balanced to attract the right range of buyers.
# A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

# Given an integer array art_pieces representing the value of each art piece,
# write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

# A subsequence is a sequence derived 

# Example Usage:

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))
# Example Output:

# 5
# Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

# 2
# 0


def find_balanced_subsequence(art_pieces):
    freq_map = Counter(art_pieces)
    maxLength = 0
    for key, value in freq_map.items():
        if (key + 1) in freq_map:
            maxLength = max(maxLength, value + freq_map[key + 1])
    return maxLength
                
'''
Problem 2: Verifying Authenticity

Your art gallery has just been shipped a new collection of numbered art pieces,
and you need to verify their authenticity. The collection is considered "authentic"
if it is a permutation of an array base[n].

The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array
of length n + 1 containing the integers from 1 to n - 1 exactly once, and the
integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

Write a function is_authentic_collection that accepts an array of integers
art_pieces and returns True if the given array is an authentic array, and
otherwise returns False.

Note: A permutation of integers represents an arrangement of these numbers.
For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of
numbers 1, 2, and 3.

Example Usage:

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
Example Output:

False
Example 1 Explanation: Since the maximum element of the array is 3, the only 
candidate n for which this array could be a permutation of base[n], is n = 3. 
However, base[3] has four elements but array collection1 has three. Therefore, 
it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

True
Example 2 Explanation:  Since the maximum element of the array is 3, the only 
candidate n for which this array could be a permutation of base[n], is n = 3. 
It can be seen that collection2 is a permutation of base[3] = [1, 2, 3, 3] 
(by swapping the second and fourth elements in nums, we reach base[3]).
 Therefore, the answer is true.

True
Example 3 Explanation; Since the maximum element of the array is 1, 
the only candidate n for which this array could be a permutation of base[n], 
is n = 1. It can be seen that collection3 is a permutation of base[1] = [1, 1].
 Therefore, the answer is true.

'''

def is_authentic_collection(art_pieces):
    max = max(art_pieces)
    if len(art_pieces) != (max+1):
        return False

    freq = {}

    for piece in art_pieces:
        if piece in freq:
            freq[piece] = freq.get(piece) + 1
        
        else:
            freq[piece] = 1
        
        if freq[piece] == 2:
            return False
    
    return True

    
    # 1,2,...500 ->501 number