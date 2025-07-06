'''
Problem 1: Villager Class
A class constructor is a special method or function that is used to create and initialize 
a new object from a class. Define the class constructor __init__() for a new class Villager 
that represents characters in the game Animal Crossing. The constructor accepts three required 
arguments: strings name, species, and catchphrase. The constructor defines four properties for a 
Villager:

name, a string initialized to the argument name
species, a string initialized to the argument species
catchphrase, a string initialized to the argument catchphrase
furniture, a list initialized to an empty list
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
Example Usage:

apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)
Output:

Apollo
Eagle
pah
[]
'''

        
'''
Problem 2: Add Furniture
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the villager’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette",
"rattan armchair", "kotatsu", or "cacao tree".

class Villager:
    # ... methods from previous problems
	
    def add_item(self, item_name):
        pass
Example Usage:

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
Output:

[]
["acoustic guitar"]
["acoustic guitar", "cacao tree"]
["acoustic guitar", "cacao tree"]
'''

'''
Problem 3: Group by Personality
The Villager class has been updated below to include the new string attribute personality 
representing the character's personality type.

Outside of the Villager class, write a function of_personality_type(). Given a list of Villager
instances townies and a string personality_type as parameters, return a list containing the names
of all villagers in townies with personality personality_type. Return the names in any order.

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
	
def of_personality_type(townies, personality_type):
    pass
Example Usage:

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
Example Output:

['Bob', 'Stitches']
[]
'''
'''
Problem 4: Telephone
The Villager constructor has been updated to include an additional attribute neighbor. 
A villager's neighbor is another Villager instance and represents their closest neighbor. 
By default, a Villager's neighbor is set to None.

Given two Villager instances start_villager and target_villager, write a function message_received() 
that returns True if you can pass a message from the start_villager to the target_villager through a 
series of neighbors and False otherwise.

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems
	
def message_received(start_villager, target_villager):
    pass
Example Usage:

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))
Example Output:

True
Example 1 Explanation: Isabelle can pass a message to her neighbor, Tom Nook. Tom Nook can then pass the 
message to his neighbor, KK Slider. KK Slider is the target, therefore the function should return True.

False
Example 2 Explanation: KK Slider doesn't have a neighbor, so you cannot pass a message to Isabelle from 
KK Slider. 
'''

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        self.personality = personality
        self.neighbor = neighbor
    
    def add_item(self, item_name):
        valid_list = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        valid_values = set(valid_list)
        if item_name in valid_values:
            self.furniture.append(item_name) # P1 Time, Space complexities: O(1)

def of_personality_type(townies, personality_type): # P2 Time, Space complexities: O(n)
    result = []
    for villager in townies:
        if villager.personality == personality_type:
            result.append(villager.name)
    return result

def message_received(start_villager, target_villager):
    current = start_villager
    while current != None:
        if current == target_villager:
            return True
        current = current.neighbor
    return False

'''
Problem 5: Linked Up
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces 
of data sequentially. The difference between a linked list and a normal list lies in how each element 
is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according 
to the order they appear in the list. If we know where the first element of the list is stored, it’s 
really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. 
Each node may be stored in an unrelated memory location. To connect nodes together into a sequential 
list, each node stores a reference or pointer to the next node in the list.

Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> 
isabelle.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints
 the values of the list has also been provided for testing purposes.

# Add code here to link the above nodes
Example Usage:

print_linked_list(kk_slider)
Example Output:

K.K. Slider -> Harriet -> Saharah -> Isabelle
'''
'''
Problem 6: Got One!
Imagine that behind the scenes, Animal Crossing uses a linked list to represent the order
 fish will appear to a player who is fishing in the river. The head of the list represents 
 the next fish that a player will catch if they keep fishing.

Write a function catch_fish() that accepts the head of a list. The function should:

Print the name of the fish in the head node using the format "I caught a <fish name>!".
Remove the first node in the list.
The function should return the new head of the list. If the list is empty, print "Aw! Better 
luck next time!" and return None.

A function print_linked_list() which accepts the head, or first element, of a linked list and 
prints the list data has also been provided for testing purposes.

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    pass
Example Usage:

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))
Example Output:

Carp -> Dace -> Cherry Salmon
I caught a Carp!
Dace -> Cherry Salmon
Aw! Better luck next time!
None
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if not head.next:
        return 'Aw! Better luck next time!'
    print(f"I caught a {head.value}")
    

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
kk_slider.next.next = saharah
kk_slider.next.next.next = isabelle

harriet = None
saharah = None
isabelle = None

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))