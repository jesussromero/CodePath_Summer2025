'''
Problem 1: Can Rebook Flight

Oh no! You're flight has been cancelled and you need to rebook. Given an adjacency matrix of today's flights flights 
where each flight is labeled 0 to n-1 and flights[i][j] = 1 indicates that there is an available flight from location 
i to location j, return True if there exists a path from your current location source to your final destination dest. 
Otherwise return False.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your 
solution has the stated time complexity.

def can_rebook(flights, source, dest):
    pass

Example Usage:

flights1 = [
          j
       0  1  2   

  0   [0, 1, 0], # Flight 0
i 1   [0, 0, 1], # Flight 1
  2   [0, 0, 0]  # Flight 2
]        

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 

Example Output:

True
False

'''

def can_rebook(flights, source, destination):
    connections = []
    for x, flight in enumerate(flights):
        #1. We iterate over the row and check for 1's. We will append the connections
        for i in range(len(flight)):
            if flight[i] == 1:
                connections.append([x, i])
    #2. Once we have the connection list, look for the combination in which the second element and first element are the same
    
   
    result = []
    # while i != len(connections)-1:
    #     curr = connctions[i]
    #     after = connections[i+1]
    #     if curr[1] == after[0]:
    #         result.append([curr[0], after[1]])
    i = 0
    while i < 100000:
        for el1 in connections:
            for el2 in connections:
                if el1 == el2:
                    continue

                if el1[1] == el2[0]:
                    result.append([el1[0], el2[1]])
        i += 1
                

    print(connections)
    print(result)
    return ([source, destination] in result) or ([destination, source] in result)
    # 
    # [[0,1], [4,2], [1,4]]
    # [[0,4], [4,2]]
    # [[0,2]]

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

flights3 = [
#    0  1  2  3  4
    [0, 0, 1, 0, 0], # 0->2
    [1, 0, 0, 0, 0], # 1->0
    [0, 0, 0, 0, 1], # 2->4
    [0, 1, 0, 0, 0], # 3->1
    [0, 0, 0, 1, 0]  # 4->3
]

#print(can_rebook(flights1, 0, 2))
#print(can_rebook(flights2, 0, 2)) 
print(can_rebook(flights3, 4, 2)) 