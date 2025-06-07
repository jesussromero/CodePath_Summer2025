from typing import Optional

catchPhrase =  {"Pooh":"Oh bother!", 
                "Tigger": "TTFN: Ta-ta for now!", 
                "Eeyore": "Thanks for noticing me.", 
                "Christopher Robin": 	"Silly old bear."}

def welcome():
    print("Welcome to The Hundred Acre Wood!")

def greeting(name):
    print(f"Hello, {name}! Welcome to The Hundred Acre Wood!")

def CatchPhrase(key):
    return catchPhrase.get(key, "Catchphrase not found.")

def get_item(item, x) -> Optional[str]:
    if x >= len(item):
        return None
    return item[x]

def sum_honey(hunny_jars):
    total_sum = 0
    for x in hunny_jars:
        total_sum += x
    return total_sum

def doubled(hunny_jars):
    for x in range(len(hunny_jars)):
        hunny_jars[x] *= 2

def count_less_than(race_times, threshold):
    Ct = 0
    for n in race_times:
        Ct += 1 if n < threshold else 0
    return Ct

def print_todo_list(task):
    print("Pooh's To Dos:")
    for i in range(1, len(task)+1):
        print(f'{i}: {task[i-1]}')

def can_pair(item_quantities):
    for item in item_quantities:
        if item%2 != 0:
            return False
    return True

def split_haycorns(quantity):
    results = []
    for i in range(1, quantity+1):
        if quantity%i == 0:
            results.append(i)
    return results 

def tiggerfy(s):
    s = s.lower()
    result = ''
    avoid_letters = {'t', 'i', 'g', 'e', 'r'}
    
    for letter in s:
        if letter not in avoid_letters:
            result += letter

    print(result)



if __name__ == "__main__":
    welcome()
    greeting("Michael")
    print(CatchPhrase("Pooh"))

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 5

    print(get_item(items, 2))

    hunny_jars = [2, 3, 4, 5]
    print(sum_honey(hunny_jars))

    hunny_jars = []
    print(sum_honey(hunny_jars))
    
    hunny_jars = [1, 2, 3]
    doubled(hunny_jars)
    print(hunny_jars)

    race_times = [1, 2, 3, 4, 5, 6]
    threshold = 7
    print(count_less_than(race_times, threshold))

    task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    print_todo_list(task)

    task = []
    print_todo_list(task)

    item_quantities = [2, 4, 6, 8]
    print(can_pair(item_quantities))

    item_quantities = [1, 2, 3, 4]
    print(can_pair(item_quantities))

    quantity = 6
    print(split_haycorns(quantity))

    quantity = 1
    print(split_haycorns(quantity))

    s = "suspicerous"
    tiggerfy(s)

    s = "Trigger"
    tiggerfy(s)

    s = "Hunny"
    tiggerfy(s)