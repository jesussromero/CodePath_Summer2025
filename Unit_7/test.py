import random

def limit_testing_sets(upper_bound):
    nums = list(range(1, upper_bound+1))
    random.shuffle(nums)
    print(nums)
    my_set = set(nums)
    my_list = list(my_set)
    print(my_list)
    sorted_list = my_list == sorted(my_list)
    print(f"Set of size {upper_bound} appears sorted? {sorted_list}")


limit_testing_sets(20)

