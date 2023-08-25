class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            
            current_node.next = newNode

        self.length += 1
        return newNode
    
    def pop(self):
        if self.head is None:
            return 'List is empty'
        
        if self.length == 1:
            self.head = None
        else:
            temp = self.head # 2 -> 3 -> 5
            while temp.next.next is not None:
                temp = temp.next

            temp.next = None
        
        self.length -= 1


    def shift(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length+=1

    def unshift(self):
        if self.head is None:
            return
        
        if self.length == 1:
            self.head = None
        else:
            self.head = self.head.next

        self.length -= 1

    def reverse(self):
        # 1 -> 2 -> 3 -> 4 -> 5
        # we would take temp_head and will store 1 to it.
        # we would make temp_head.next = None;
        # will assing it to new head like new_head = temp_head
        # next time will take 2 
        # this time will make its next item null and assing our new_head to it to next property and then
        # will reassign that to new_head

        current_head = self.head;

        new_head = None;

        while current_head is not None:
            temp_head = current_head
            current_head = current_head.next;
            temp_head.next = new_head
            new_head = temp_head

        self.head = new_head
        return self;

    def __len__(self):
        return self.length
    
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

example_list = LinkedList()
example_list.push(3)
example_list.push(4)
example_list.push(22)
example_list.push(12)
example_list.push(10)
example_list.push(1033)

example_list.shift(1033)
example_list.shift(2)
example_list.pop()
example_list.push(3)

# for item in example_list:
#     print(item)

# print(len(example_list))





















### Other And Old ###

def reverse_linked_list(l_list):
    if l_list.head is None:
        return
    if l_list.head.next is None:
        return l_list.head
    
    # bruteforce:

    reversed_linked_list = LinkedList()
    current_list = l_list.head;

    while current_list is not None:
        reversed_linked_list.shift(current_list.data)
        current_list = current_list.next
    
    return reversed_linked_list
    # 1 -> 2 -> 3 -> 4 -> 5
    # we would take temp_head and will store 1 to it.
    # we would make temp_head.next = None;
    # will assing it to new head like new_head = temp_head
    # next time will take 2 
    # this time will make its next item null and assing our new_head to it to next property and then
    # will reassign that to new_head

    current_head = list.head;

    new_head = None;

    while current_head is not None:
        temp_head = current_head
        current_head = current_head.next;
        temp_head.next = new_head
        new_head = temp_head

    list.head = new_head
    return list;