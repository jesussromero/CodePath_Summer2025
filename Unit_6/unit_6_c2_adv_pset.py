'''
Problem 1: Next in Queue
Each user on a music app should have a queue of songs to play next. Implement the class 
Queue using a singly linked list. Recall that a queue is a First-In-First-Out (FIfO) 
data structure where elements are added to the end (the tail) and removed from the front (the head).

Your queue must have the following methods:

__init()__: Initializes an empty queue (provided)
enqueue(): Accepts a tuple of two strings (song, artist) and adds the element with the specified 
tuple to the end of the queue.
dequeue(): Removes and returns the element at the front of the queue. If the queue is empty, 
returns None.
peek(): Returns the value of the element at the front of the queue without removing it. 
If the queue is empty, returns None.
is_empty(): Returns True if the queue is empty, and False otherwise.
'''
# U: We are going to implement a Queue class and its methods using a linked list
# M: Linked Lists
# P: Declare a class, we are going to implement the methods one by one
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front == None:
            return True
        return False

    def enqueue(self, value):
        if self.front == None:
            self.front = Node(value)
        else:
            if self.rear == None:
                self.rear = Node(value)
                self.front.next = self.rear
            else:
                self.rear.next = Node(value)
                self.rear = self.rear.next

        return
    
    def dequeue(self):
        value = self.front.value
        self.front = self.front.next
        return value
    
    def peek(self):
        return self.front.value
    

'''
Problem 2: Merge Playlists

You are given the head of two linked lists, playlist1 and playlist2 with lengths n and m respectively. Remove playlist1's nodes from the ath to the bth node and put playlist2 in its place. Assume the lists are 0-indexed.

The blue edges and nodes in the figure below indicate the result:

Merged playlists

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    pass

Example Usage:

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))

Example Output:

('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant')
-> ('Empty', 'Kevin Abstract')

'''

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    
    # iterate up to node a-1
    counter1 = playlist1
    counter1_prev = None
    for i in range(a):
        counter1_prev = counter1
        counter1 = counter1.next
    
    # change connection of node a-1 to node 0
    counter1_prev.next = playlist2
    # iterate up to node b+1
    for i in range(a,b,1):
        counter1 = counter1.next
    counter1 = counter1.next

    counter2 = playlist2
    counter2_prev = None
    while counter2:
        counter2_prev = counter2
        counter2 = counter2.next
    # change connection of node m-1 to b+1
    counter2_prev.next = counter1
    
    return playlist1

playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))
#('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant')
#-> ('Empty', 'Kevin Abstract')
print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))