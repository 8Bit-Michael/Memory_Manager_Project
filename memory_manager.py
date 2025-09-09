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
        size = total_size
        is_free = True
        self.head = MemoryBlock(start, size, is_free, None, self) # The head of the linked list representing memory blocks.


    def allocate(self, size):
        pass

    def free(self, address):
        pass

    def merge_free_blocks(self):
        pass

    def display_memory(self):
        pass
