class MemoryBlock:
    def __init__(self, start, size, is_free, next):
        self.start = start
        self.size = size
        self.is_free = is_free
        self.next = next

class MemoryManager:
    
    def initialize_memory(self, total_size):
        if total_size > 1:
            print('Initializing memory:', total_size)
        else:
            print('You must have more than one block of memory.')

    def allocate(self, size):
        pass

    def free(self, address):
        pass

    def merge_free_blocks(self):
        pass

    def display_memory(self):
        pass

manager = MemoryManager()

manager.initialize_memory(1024)