'''
Problem 3: Segmenting Protein Chains for Analysis
As a biochemist, you are analyzing a long protein chain represented by a singly linked list, 
where each node is an amino acid. 
For a specific experiment, you need to split this protein chain into k consecutive segments 
for separate analysis. Each segment should be as equal in length as possible, with no two segments 
differing in size by more than one amino acid.

The segments should appear in the same order as the original protein chain, and segments earlier in 
the list should have a size greater than or equal to those occurring later. If the protein chain 
cannot be evenly divided, some segments may be an empty list.

Write a function split_protein_chain() that takes the head of the linked list protein and an integer k,
and returns an array of k segments.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.
'''
import math

def get_length(head):
    length = 0
    curr_node = head
    while curr_node:
        length += 1
        curr_node = curr_node.next
    return length

def split_protein_chain(protein, k):
    # Plan
    # Get the length of the list
    length = get_length(protein)

    # Get elements per segment
    elements_per_segment = math.ceil(length / k)

    segments_created = 0
    while (segments_created < k):
        
        segments_created += 1

    
    # Return a list of nodes
    pass