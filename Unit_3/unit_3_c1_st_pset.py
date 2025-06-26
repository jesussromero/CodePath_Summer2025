from collections import deque

'''
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. 
Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, 
and {} for links. You are given a string representing a post's content, and your task is to determine 
if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.

Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Example Output:

True
True
False

'''

# U: We are given a string that contains either parentheses, brackets, or curly braces. In order for
#    the input to be valid, each character input needs to have a corresponding closing form of itself
#    We return a boolean
# M: We can use a Stack to keep track of what we have in so far. If the last popped element in the stack
#    is equal to its closing, then we return False
def is_valid_post_format(posts):
    invalid_starting = ["}", "]", ")"]
    valid_start = {")":"(", "]":"[", "}":"{"}
    my_helper = []
    # Immediately return if it starts with a closing bracket or length is less than 1
    if posts[0] in invalid_starting or len(posts) <= 1:
        return False
    # Applying logic described above
    for ch in posts:
        if ch in valid_start.values():
            my_helper.append(ch)
        else:
            if not my_helper or my_helper.pop() != valid_start.get(ch):
                return False
    return True

        
'''
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received.
However, for a special feature, you need to reverse the order of comments before displaying them.
Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
    pass

Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']

'''
# U: We receive a list of strings, where each element is a comment. We output the reversed string
# M: We can use a queue because it follows the FIFO rule, which is exactly what we need
def reverse_comments_queue(comments):
    my_queue = deque()
    result = []
    for comment in comments:
        my_queue.append(comment)
    
    for element in range(len(my_queue)):
        result.append(my_queue.pop())

    return result # works!

'''
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical,
meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case.
Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
    pass

Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

Example Output:

True
False
'''

# U: The problem will give us a string. We have to check if once it doesn't have any especial chars
#    the string is the same if read the same forwards or backwards
# M: It explicitly asks for us to use a double pointer. My strat would be to first remove especial chars
#    and then lower everything. After that, use the double pointer strat.

def is_symmetrical_title(title):
    title = title.lower()
    title = title.replace(" ", "")
    left = 0
    right = len(title) - 1

    for ch in title:
        if title[left] != title[right]:
            return False
        else:
            left += 1
            right -= 1
    return True # Works

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 