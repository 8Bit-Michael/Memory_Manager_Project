class MemoryBlock:
    def __init__(self, start, size, is_free, next_block, memory_block):
        self.start = start
        self.size = size
        self.is_free = is_free
        self.next = next_block
        self.memory_block = memory_block

class MemoryManager:
    def __init__(self, total_size):
        self.total_size = total_size
        self.initialize_memory(total_size)
    
    def initialize_memory(self, total_size):
        self.head = MemoryBlock(0, total_size, True, None, self)
    
    def allocate(self, size):
        current = self.head
        while current:
            if current.is_free and current.size >= size:
                if current.size == size:
                    current.is_free = False
                    return current.start
                else:
                    remaining_block = MemoryBlock(
                        start=current.start + size,
                        size=current.size - size,
                        is_free=True,
                        next_block=current.next,
                        memory_block=self
                    )
                    current.size = size
                    current.is_free = False
                    current.next = remaining_block
                    return current.start
            current = current.next
        print("Allocation failed: Not enough memory.")
        return None
    
    def display_memory(self):
        current = self.head
        while current:
            print(f"[Start: {current.start}, Size: {current.size}, Free: {current.is_free}]")
            current = current.next

    def free(self, address): 
        current = self.head
        while current: # While there is another node pointed to:
            if current == address: # If the node is equal to what the user is searching for:
                current.is_free = True # The node is defined as free.
            else:
                current = current.next # Go to the next node if False.     

    def merge_free_blocks(self):
        free_space = [] # The list of free nodes
        current = self.head # Start with the head as the current
        while current: # While there is a node
            if current.is_free: # If the current node has no data
                free_space.append(current) # Append the node to the list of free_space?
                if current.next: # If there is a pointer to another node
                    current = current.next # Switch to that next node
                else:
                    pass # If there are other nodes in the free_space list add them? How do you add them and delete them?
                    # Remove the leftover node  
        
