class MemoryBlock:
    def __init__(self, start, size, is_free, next, memory_block):
        self.start = start
        self.size = size
        self.is_free = is_free
        self.next = None
        self.memory_block = memory_block


class MemoryManager:
    def __init__(self, total_size):
        self.total_size = total_size
        self.initialize_memory(total_size) # Initialize memory with a single large free block.
    
    def initialize_memory(self, total_size):
        start = 0
        size = total_size # Size = The size of the new block.
        is_free = True
        self.head = MemoryBlock(start, size, is_free, None, self) # The head of the linked list representing memory blocks.


    def allocate(self, size): # Size = The size of code set aside for something.
        current = self.head
        while current: # Make this 'traverse' somehow.
            if current.next == True: # If there is a node/memory block pointer.
                current = current.next # Switch from the head to the next block? Could be assigning the next as the head.
                if self.current == True and self.size == size: # If there is a new current and it's equal to the requested size.
                    self.current = size # Make the current node become the requested block size.
                else:
                    continue # Continue going through.
            else:
                return

        if self.size > size:
            is_free = True
            start = 0 # Start off with a value of 0? But zero is still a value?
            head_1 = MemoryBlock(start, (size), is_free, None, self)
            head_2 = MemoryBlock(start, (self.size - size), is_free, None, self)
    def free(self, address):
        pass

    def merge_free_blocks(self):
        pass

    def display_memory(self):
        pass
