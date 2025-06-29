from collections import deque
'''
Problem 1: Count Unique Characters in a Script
Given a dictionary where the keys are character names and the values are lists of their dialogue lines,
count the number of unique characters in the script.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys)) 
Example Output:

3
2
'''
def count_unique_characters(script):
    mySet = set()
    for key in script:
        mySet.add(key)
    return len(mySet) # O(n) for both space and time complexity
 
'''
Problem 2: Find Most Frequent Keywords
Identify the most frequently used keywords from a dictionary where the keys are scene names 
and the values are lists of keywords used in each scene. Return the keyword that appears the 
most frequently across all scenes. If there is a tie, return all the keywords with the highest 
frequency.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def find_most_frequent_keywords(scenes):
  pass
Example Usage:


Example Output:

['action', 'hero']
['love', 'drama']
'''
# Time complexity: O(n)
# Space complexity: O(n)
def find_most_frequent_keywords(scenes):
    frequency_dict = dict()

    for key,value in scenes.items():
        for keyword in value:
            frequency_dict[keyword] = 1 if not keyword in frequency_dict else frequency_dict[keyword] + 1

    # Iterate through dictionary, extracting max value. Keep track of 
    max_value = max(frequency_dict.values())

    result = []

    for key,value in frequency_dict.items():
        if value == max_value:
            result.append(key)

    return result
    
'''
Problem 3: Track Scene Transitions
Given a list of scenes in a story, use a queue to keep track of the transitions from one scene 
to the next. You need to simulate the transitions by processing each scene in the order they appear 
and print out each transition from the current scene to the next.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

Example Usage:

scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)
Example Output:

Transition from Opening to Rising Action
Transition from Rising Action to Climax
Transition from Climax to Falling Action
Transition from Falling Action to Resolution

Transition from Introduction to Conflict
Transition from Conflict to Climax
Transition from Climax to Denouement
'''

def track_scene_transitions(scenes):
    prev = ''
    my_deque = deque(scenes)
    for element in scenes:
        if not prev:
            prev = my_deque.popleft()
        else:
            print(f'Transition from {prev} to {my_deque[0]}')
            prev = my_deque.popleft()
            # Space: O(n)
            # Time: O(n)
'''
Problem 4: Organize Scene Data by Date
Given a list of scene records, where each record contains a date and a description, 
sort the list by date and return the sorted list. Each record is a tuple where the first element 
is the date in YYYY-MM-DD format and the second element is the description of the scene.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def organize_scene_data_by_date(scene_records):
  pass
Example Usage:

scene_records = [
    ("2024-08-15", "Climax"),
    ("2024-08-10", "Introduction"),
    ("2024-08-20", "Resolution"),
    ("2024-08-12", "Rising Action")
]
print(organize_scene_data_by_date(scene_records))

scene_records = [
    ("2023-07-05", "Opening"),
    ("2023-07-07", "Conflict"),
    ("2023-07-01", "Setup"),
    ("2023-07-10", "Climax")
]
print(organize_scene_data_by_date(scene_records))
Example Output:

[('2024-08-10', 'Introduction'), ('2024-08-12', 'Rising Action'), ('2024-08-15', 'Climax'), ('2024-08-20', 'Resolution')]
[('2023-07-01', 'Setup'), ('2023-07-05', 'Opening'), ('2023-07-07', 'Conflict'), ('2023-07-10', 'Climax')]
'''


def organize_scene_data_by_date(scene_records):
    sorted_record=[]
    for record in scene_records:
        sorted_record.append(record)
    sorted_record.sort() # Time: O(n log n), Space: O(n)
    return sorted_record

'''
Problem 5: Filter Scenes by Keyword
Scenes often contain descriptions that set the tone or provide important information. 
However, certain scenes may need to be filtered out based on keywords that are either 
irrelevant to the current narrative path or that the user wishes to avoid. Write a function 
that, given a list of scene descriptions and a keyword, filters out the scenes that contain the 
specified keyword.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.

def filter_scenes_by_keyword(scenes, keyword):
  pass
Example Usage:

scenes = [
    "The hero enters the dark forest.",
    "A mysterious figure appears.",
    "The hero finds a hidden treasure.",
    "An eerie silence fills the air."
]
keyword = "hero"

filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
print(filtered_scenes)

scenes = [
    "The spaceship lands on an alien planet.",
    "A strange creature approaches the crew.",
    "The crew prepares to explore the new world."
]
keyword = "crew"

filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
print(filtered_scenes)
Example Output:

['An eerie silence fills the air.', 'A mysterious figure appears.']
['The spaceship lands on an alien planet.']
'''


def filter_scenes_by_keyword(scenes, keyword):
    result = []
    for sentence in scenes:
        if not keyword in sentence:
            result.append(sentence)
    return result # Time: O(n*m), Space: O(n)


'''
Problem 6: Manage Character Arcs
Character arcs are crucial to maintaining a coherent narrative. These arcs often involve a series 
of events or changes that must occur in a specific order. As the story progresses, you may need to add,
 remove, or update these events to ensure the character's development follows the intended sequence.

Your task is to simulate managing character arcs using a stack. Given a series of events representing a
 character's development, use a stack to process these events. Add events to the stack as they occur 
 and pop them off when they are completed or no longer relevant, ensuring that the character arc
 maintains the correct sequence.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def manage_character_arc(events):
  pass
Example Usage:

events = [
    "Character is introduced.",
    "Character faces a dilemma.",
    "Character makes a decision.",
    "Character grows stronger.",
    "Character achieves goal."
]

processed_arc = manage_character_arc(events)
print(processed_arc)

events = [
    "Character enters a new world.",
    "Character struggles to adapt.",
    "Character finds a mentor.",
    "Character gains new skills.",
    "Character faces a major setback.",
    "Character overcomes the setback."
]

processed_arc = manage_character_arc(events)
print(processed_arc)
Example Output:

['Character is introduced.', 'Character faces a dilemma.', 'Character makes a decision.', 'Character grows stronger.', 'Character achieves goal.']
['Character enters a new world.', 'Character struggles to adapt.', 'Character finds a mentor.', 'Character gains new skills.', 'Character faces a major setback.', 'Character overcomes the setback.']
'''
def manage_character_arc(events):
    stack=[]
    for event in events:
        stack.append(event)

    return stack

events = [
    "Character is introduced.",
    "Character faces a dilemma.",
    "Character makes a decision.",
    "Character grows stronger.",
    "Character achieves goal."
]

processed_arc = manage_character_arc(events)
print(processed_arc)

events = [
    "Character enters a new world.",
    "Character struggles to adapt.",
    "Character finds a mentor.",
    "Character gains new skills.",
    "Character faces a major setback.",
    "Character overcomes the setback."
]

processed_arc = manage_character_arc(events)
print(processed_arc)