#  A Node class represnting each element in the linked list:

class Node: # Other nodes.
    def __init__(self, data):
        self.data = data # Store the data.
        self.next = None # Pointer to the next node (defaults to None)

# Linked list class:

class LinkedList:
    def __init__(self):
        self.head = None # The head node.

    def append(self, data):

        if self.head is None: # The first node gets assigned as the head.
            new_node = Node(data)
            self.head = new_node
            return
        
    # Else/after a head is assigned
    #  keep traversing and appending new nodes.
        new_node = Node(data)
        current = self.head
        while current.next: # While there is still a pointer (tails have none):
            current = current.next # Assign the data to the next node.
        current.next = new_node


    def display(self):  
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") # By the time you reach the end there is no more pointer.

    # Appending a node(but it goes to the back of the list)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key): # key is the val of the node to be deleted.
        current = self.head # Start at the head.
        prev = None # There should be no previous node when your on the head.

        # Case 1: List is empty
        if not current: # If there is no head.
            return # Return so.
        
        # Case 2: The node to delete is the head.
        if current.data == key: # If the head's data is the one to be deleted
            self.head = current.next # Switch to the next node and make that the new head. 
            return
                
        # Traverse the list to find the node to delete
        while current and current.data != key: # While there's a head and the data doesn't match:
            prev = current # The previous node is now the head.
            current = current.next

        # If the key was not found, do nothing
        if not current:
            return

        # Unlink the node from the list
        if current:
            prev.next = current.next

test = LinkedList()
test.prepend(3)
test.prepend(2)
test.prepend(5)
test.append(7)
test.display()
test.delete(2)
