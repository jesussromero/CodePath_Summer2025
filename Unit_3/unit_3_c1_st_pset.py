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

'''
P4
'''

def engagement_boost(engagements):
    n = len(engagements)
    result = [0] * n
    left = 0
    right = n - 1
    position = n - 1 

    while left <= right:
        if abs(engagements[left]) > abs(engagements[right]):
            result[position] = engagements[left] ** 2
            left += 1
        else:
            result[position] = engagements[right] ** 2
            right -= 1
        position -= 1

    return result

'''
Problem 5: Content Cleaner
You want to make sure your posts are clean and professional. Given a string post of lowercase and 
uppercase English letters, you want to remove any pairs of adjacent characters where one is the 
lowercase version of a letter and the other is the uppercase version of the same letter. Keep 
removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
Example Output:

post

s
'''
# U: we receive a string as an input and are expected to output the "cleaned" string which follow 
#    the rule of not having the same character with the uppercase version of it adjacent to the right
# M: Running a for loop, adding elements to the stack. Peek for the previous element added, and if it
#    is the same as the current one but uppercase or lowercase, we pop it.
def clean_post(post):
    my_stack = []
    for ch in post:
        if not my_stack:
            my_stack.append(ch)
        else:
            if ch.islower():
                if my_stack[-1] == ch.upper():
                    my_stack.pop()
                    continue
            elif ch.isupper():
                if my_stack[-1] == ch.lower():
                    my_stack.pop()
                    continue
            my_stack.append(ch)
    return "".join(my_stack)

'''
Problem 6: Post Editor
You want to add a creative twist to your posts by reversing the order of characters in each word 
within your post while still preserving whitespace and the initial word order. Given a string post, 
use a queue to reverse the order of characters in each word within the sentence.

Example Usage:

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 
Example Output:

tsooB ruoy tnemegegna htiw esehT spit
kcehC tuo ym tseval golv
'''
# U: We are given a string and expected to reverse every word as an output
# M: We can iterate over every word and reverse it using a deque. If it's a space, we just skip the
#    iteration
def edit_post(post):
    my_deque = deque()
    result = ''
    for i in range(len(post)):
        if post[i] == " " or i == len(post)-1:
            if i == len(post)-1:
                my_deque.append(post[i])
            for j in range(len(my_deque)):
                result += my_deque.pop()
            if post[i] == " ":
                result += post[i]
            my_deque.clear()
        else:
            my_deque.append(post[i])
    return result

'''
Problem 7: Post Compare
You often draft your posts and edit them before publishing. 
Given two draft strings draft1 and draft2, return true if they are equal when both are typed 
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will remain empty.

Example Usage:

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
Example Output:

True
True
False

'''
def post_compare(draft1, draft2):
    my_stack = []
    my_stack2 = []

    for ch in draft1:
        if not my_stack:
            my_stack.append(ch)
        else:
            if (ch == "#"):
                my_stack.pop()
            else:
                my_stack.append(ch)

    for ch in draft2:
        if not my_stack2:
            my_stack2.append(ch)
        else:
            if (ch == "#"):
                my_stack2.pop()
            else:
                my_stack2.append(ch)
                 
    return my_stack == my_stack2

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 