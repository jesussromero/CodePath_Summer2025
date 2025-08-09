'''
Problem 1: Graphing Flights

The following graph represents the different flights offered by CodePath Airlines. 
Each node or vertex represents an airport (JFK - New York City, LAX - Los Angeles, DFW - Dallas Fort Worth, and ATL - Atlanta), 
and an edge between two vertices indicates that CodePath airlines offers flights between those two airports.

Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is 
represented by a string with the airport's name (ex. "JFK").

"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
# Add your code here

Example Usage:

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])

Example Output:

['JFK', 'LAX', 'DFW', 'ATL']
[['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
['LAX', 'DFW']

'''
flights = {
    'JFK': ["LAX","DFW"],
    'LAX': ["JFK"],
    'DFW': ["JFK", "ATL"],
    'ATL': ["DFW"]
}

'''
Problem 2: There and Back

As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node 
represents the ID of a different destination and flights[i] is an integer array indicating that there is a flight from 
destination i to each destination in flights[i]. Write a function bidirectional_flights() that returns True if for any flight 
from a destination i to a destination j there also exists a flight from destination j to destination i. Return False otherwise.



Example Usage:

Example 1: flights1

'flights1' graph diagram

Example 2: flights2 'flights2' graph diagram

Adjacency lists
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

Example Output:

True
False

'''














'''
Flights 1: {
0: [1, 2],
1: [0],
2: [0, 3],
3: [2]
}

Flights 2: {
0: [1, 2],
1: [],
2: [0],
3: [2]
}
'''


# Must be bidirectional for all nodes
# If one node is non-bidirectional, return False
# At the end, return True
# Brute force approach
def bidirectional_flights(flights):
    # 1. Build dictionary
    dictionary = dict()
    for i in range(len(flights)):
        dictionary[i] = flights[i]
    # 2. Create helper function to determine if any given pair of nodes are bidirectional
        # Any node is bidirectional if:
        # a. Node A contains value of node B, and node B contains value of node A
    def is_bidirectional(node_a, node_b):
        if not node_a in dictionary:
            return False
        if not node_b in dictionary:
            return False
        return node_b in dictionary[node_a] and node_a in dictionary[node_b]

    # 3. Run this helper function on every key of the dictionary
        # If any key is not bidirectional, return False
    for key, adjacency_list in dictionary.items():
        for node in adjacency_list:
            if not is_bidirectional(key, node):
                return False
            
    # 4. If it passes key check, return True
    return True
        
    
    

        



# Checking if any of the values of the adjency list of index i are in the previous stored dictionary with key 



        

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))