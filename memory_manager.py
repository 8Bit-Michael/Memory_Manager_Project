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
        memory_status = []

        while current:
            print(f"[Start: {current.start}, Size: {current.size}, Free: {current.is_free}]")
            memory_status.append((current.start, current.size, current.is_free))
            current = current.next

        allocated = sum(size for start, size, is_free in memory_status if not is_free)
        free = sum(size for start, size, is_free in memory_status if is_free)

        return f'[ALLOCATED: {allocated}] [FREE: {free}]'
    
    def get_statistics(self):
        current = self.head
        allocated = 0 # Initialize allocated memory counter
        free = 0 # Initialize free memory counter
        while current:
            if current.is_free:
                free += current.size # Add to free memory if the block is free
            else:
                allocated += current.size # Add to allocated memory if the block is not free
            current = current.next # Move to the next block
        percent_allocated = (allocated / self.total_size) * 100 if self.total_size > 0 else 0
        percent_free = (free / self.total_size) * 100 if self.total_size > 0 else 0
        return f"Percent Allocated: {percent_allocated:.2f}%, Percent Free: {percent_free:.2f}%"


    def free(self, address): # Before the issue was that if the address was invalid it would still traverse the linked list and print the success message, 
        # but also the failure message, because on the one hand it didn't find the address, but on the other hand it was coded to always print the message.
        current = self.head
        while current: # Traverse the linked list
            if address <= 0 or address >= self.total_size:
                if current.start == address: 
                    current.is_free = True
                    self.merge_free_blocks() # Merge adjacent free blocks after freeing
                    return f"Freed memory at address {address}" # Exit out of the loop once the block is found.
                current = current.next # If the current block's start address doesn't match the given address, move to the next block.
            else:
                return "Free failed: Invalid address."

    def merge_free_blocks(self):
        current = self.head
        while current and current.next: # Traverse the linked list
            if current.is_free and current.next.is_free: # If both current and next blocks are free
                current.size + current.next.size # Merge their size attributes
                current.next = current.next.next # Skip over the next block
            else: # Otherwise, just move to the next block
                current = current.next
