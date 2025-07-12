'''
Problem 1: Selective DNA Deletion
As a biologist, you are working on editing a long strand of DNA represented as a linked list 
of nucleotides. Each nucleotide in the sequence is represented as a node in the linked list, 
where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.

Given the head of the linked list dna_strand and two integers m and n, write a function 
edit_dna_sequence() that simulates the selective deletion of nucleotides in a DNA sequence.
 You will: - Start at the beginning of the DNA strand. - Retain the first m nucleotides from 
 the current position. - Remove the next n nucleotides from the sequence. - Repeat the process 
 until the end of the DNA strand is reached.

Return the head of the modified DNA sequence after removing the mentioned nucleotides.

Evaluate the time and space complexity of your solution. Define your variables and provide a 
rationale for why you believe your solution has the stated time and space complexity.
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

def edit_dna_sequence(dna_strand, m, n):
    # 1. Iterate over the linked list keeping a count. Use slow, fast technique
    slow = dna_strand
    fast = dna_strand
    count_n = 0
    count_m = 1 
    # 2. Once this count reaches m, we stop the slow list and reset the count.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        count_m += 1
        if count_m == m:
            count_m = 0
            # 3. Keep the count until n is reached. Start m count again. Repeat until fast.next is None
            while (count_n != n) and fast.next != None:
                fast = fast.next
                count_n += 1
            # 4. Connect the slow linked list with the next value if there is any
            slow.next = fast.next
            count_n = 0
    return dna_strand # Time, Space complexitites: O(n), O(1)

#dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))
# 1 -> 2 -> 6 -> 7 -> 11 -> 12
#print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

#dna_strand = Node(1, Node(3))
#print_linked_list(edit_dna_sequence(dna_strand, 2, 3))
'''
Problem 2: Protein Folding Loop Detection
As a biochemist, you're studying the folding patterns of proteins, which are represented as a sequence 
of amino acids linked together. 
These proteins sometimes fold back on themselves, creating loops that can impact their function.

Given the head of a linked list protein where each node in the linked list represents an amino acid
 in the protein, return an array with the values of any cycle in the list. A linked list has a cycle 
 if at some point in the list, the node’s next pointer points back to a previous node in the list.

The values may be returned in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
for why you believe your solution has the stated time and space complexity.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    #1. Slow and fast, fast move 2 nodes, slow moves 1 node
    #2. if fast meet slow there is a loop
    #3. if fast reach none is not a loop
    slow= protein
    fast = protein
    result =[]
    while fast!= None and fast.next!= None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        
    slow = slow.next
    result.append(slow.value)
    
    while slow!=fast:
        
        slow = slow.next
        result.append(slow.value)
    return result

#protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
#protein_head.next.next.next.next = protein_head.next 
#print(cycle_length(protein_head))

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