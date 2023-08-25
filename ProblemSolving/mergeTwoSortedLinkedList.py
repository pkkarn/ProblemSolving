from DataStructure.linked_list import LinkedList

'''
Certainly! Here's a classic interview question related to linked lists:

**Merge Two Sorted Linked Lists**

Given two sorted linked lists, merge them to form a single sorted linked list.

**Input**:
- `l1`: The head of the first sorted linked list.
- `l2`: The head of the second sorted linked list.

**Output**:
- Return the head of the merged sorted linked list.

**Example**:

```
Input:
            i
l1: 1 -> 3 -> 5
l2: 2 -> 4 -> 6 
            j

new_list = 1,2,3,4,5,6

- if length of i < length of l1 and j < length of l
- i < j then new_list will be i else j and increment it.
- and finally print all the left items

Explanation: 


Output:
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

Can you provide a solution to merge these two linked lists in a way that maintains the sorted order?

(Note: Depending on the proficiency level of the candidate, you can modify the question to have additional constraints or conditions, such as merging the lists in-place without creating a new list, handling edge cases, etc.)
'''


def merge_sorted_list(list1, list2):
    new_list = LinkedList()

    i = list1.head;
    j = list2.head;
    
    while i is not None and j is not None:
        if i.data <= j.data:
            new_list.push(i.data)
            i = i.next
        else:
            new_list.push(j.data)
            j = j.next
    

    while i is not None:
        new_list.push(i.data)
        i = i.next

    while j is not None:
        new_list.push(j.data)
        j = j.next

    return new_list