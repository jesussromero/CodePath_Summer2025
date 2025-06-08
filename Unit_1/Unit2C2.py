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