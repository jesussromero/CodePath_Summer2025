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
# M: We can use a Stack to keep track of what we have in so far. So we would add each character to th3
#    stack.
def is_valid_post_format(posts):
    invalid_starting = ["}", "]", ")"]
    valid_start = {")":"(", "]":"[", "}":"{"}
    my_stack = []
    # Immediately return if it starts with a closing bracket 
    if posts[0] in invalid_starting or len(posts) <= 1:
        return False
    # Iterate over all of the characters in the string
    for char in posts:
        

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))