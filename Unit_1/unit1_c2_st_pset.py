def nana(x):
    #step 1: repeat x times
    #step 2: print "na"
    #step 3: print batman
    nanana = ''
    batman = 'batman!'

    if x <= 0: return print(batman)

    for i in range(x):
        nanana += 'na'

    nanana = nanana + ' ' + batman
    print(nanana)

#P2:

# reverse_sentence() -> takes a string
# output: returns string in reversed order

# splitting the sentence into words only
# output = sentence.split(" ")

# Edge Case 1: If only one char, return that

def reverse_sentence(x):
    word_list = x.split(" ")
    results = ''
    # Edge Case 1: If only one char, return that
    if len(word_list) <= 1:
        return x
    # range(start,stop,step)
    for i in range(len(word_list)-1, -1, -1):
        print(word_list[i], end=" ")
    
    return results
     
# min nums
# max nums 
# if nums != max or min 
def goldilocks_approved(nums):
    minimum, maximum = min(nums), max(nums)
    
    for i in nums:
        if (i != minimum) and (i != maximum):
            return print(i)

    return print(-1)

#delete minin
def delete_minimum_elements(hunny_jar_sizes):
    results = []

    #while len(hunny_jar_sizes) >= 0:
    for i in range(len(hunny_jar_sizes)):
        minimum = min(hunny_jar_sizes)
        results.append(minimum)
        hunny_jar_sizes.remove(minimum)

    return print(results)
        
#hunny_jar_sizes = [5, 3, 2, 4, 1]
#delete_minimum_elements(hunny_jar_sizes)

#hunny_jar_sizes = [5, 2, 1, 8, 2]
#delete_minimum_elements(hunny_jar_sizes)


# modulo strips last element
# floor division removes it
def sum_of_digits(num):
    result = 0
    while num > 0:
        result += num%10
        num = num//10
    return print(result)

#num = 423
#sum_of_digits(num)

#num = 4
#sum_of_digits(num)



# if word = bouncy and flouncy +1
# if word = trouncy and pouncy -1
# result

def final_value_after_operations(operations):
    tigger = 1
    for word in operations: 
        if (word == "bouncy") or (word == "flouncy"):
            tigger += 1
        if (word == "trouncy") or (word == "pouncy"):
            tigger -=1
    return print(tigger)    
              
    
#operations = ["trouncy", "flouncy", "flouncy"]
#final_value_after_operations(operations)

#operations = ["bouncy", "bouncy", "flouncy"]
#final_value_after_operations(operations)

# if the first letter of each word concatenated is equal to s, then it's an acronym
def is_acronym(words, s):
    result = ''
    if len(words) < 1:
        return False

    for word in words:
        result += word[0]
    
    if result == s:
        return True
    return False

# input: nums -> list of numbers
# output: number of operations to make every number in nums divisible by 3
# strat: Use modulus to determine how many steps are needed to make a number divisible by 3

# 4 % 3 = 1, if it is 1, we substract 1
# 5 % 3 = 2, if it's 2, we add 1

def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if (num % 3 == 1) or (num % 3 == 2):
            count += 1
    return print(count)


# Make a new list of elements that are in list1 but not in list2, and reverse
# input : list1, list2
# output: list1 where all elements of list1 but not in list2, 
# list2 where all elements of list2 but not iun list 1

def exclusive_elemts(lst1, lst2):
    result_lst1 = []
    for i in lst1:
        if i not in lst2:
            result_lst1.append(i)
        
    for j in lst2:
        if j not in lst1:
            result_lst1.append(j)

    return print(result_lst1)


# input: 2 different strings/words
# output: a combined string where we alternate each letter from each string
# strat: run a for loop and start adding the word at index i
def merge_alternately(word1, word2):
    result = ''
    #base cases
    if word1 == '':
        return word2
    if word2 == '':
        return word1
    # hola
    # alexandria
    for i in range(len(word1)):
        if (len(word1) > 0) and (len(word2) > 0):
            result += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
    if len(word1) > 0:
        result += word1
    if len(word2) > 0:
        result += word2
    return print(result)

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)
#"woozle"
#"heffalump"
#"eeyore"