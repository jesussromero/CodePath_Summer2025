'''
Problem 1: Manage Performance Stage Changes

At a cultural festival, multiple performances are scheduled on a single stage.

However, due to last-minute changes, some performances need to be rescheduled or canceled.

The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action.

The actions can be:

- "Schedule X": Schedule a performance with ID X on the stage.
- "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
- "Reschedule": Reschedule the most recently canceled performance to be the next on stage.

Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

Example Output:

["A", "C", "B", "D"]
[]
["Z"]
'''
# U: We are receiving a list of instructions. Each instruction performs an action and we return the 
#    finished list of artists
# M: We can iterate, read the first word and perform the action. For scheduling, we can use a stack
#    and keep a temporary stack if cancel is used.
def manage_stage_changes(changes):
    temp_stack = []
    my_stack = []
    for action in changes:
        if action[0].lower() == 's':
            my_stack.append(action[9])
        elif action[0].lower() == 'c':
            temp_stack.append(my_stack.pop())
        elif action[0].lower() == 'r':
            my_stack.append(temp_stack.pop())
    return my_stack # Works

'''
Problem 2: Queue of Performance Requests
You are organizing a festival and want to manage the queue of requests to perform.
Each request has a priority. Use a queue to process the performance requests in the order they arrive 
but ensure that requests with higher priorities are processed before those with lower priorities.
Return the order in which performances are processed.

Example Output:

['Music', 'Dance', 'Drama']
['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']
'''

# U: We are give
def process_performance_requests(requests):
    pass


print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
