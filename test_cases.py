from memory_manager import MemoryManager

def test_memory_initialization():
    print("=== Test: Memory Initialization ===")
    global manager
    manager = MemoryManager(1024)
    assert manager.total_size == 1024
    assert manager.head.size == 1024
    assert manager.head.is_free is True
    assert manager.head.start == 0
    assert manager.head.next is None

    current = manager.head
    while current:
        print(f"Block Start: {current.start}, Size: {current.size}, Is Free: {current.is_free}")
        current = current.next
    print()

def test_allocation():
    print("=== Test: Allocation ===")
    manager.allocate(300)
    manager.display_memory()
    assert manager.head.start == 0 # Make the start of the allocated node become 0, making it the head, so all you have to do is check the head.

def test_free(addr):
    print("=== Test: Free ===")
    manager.display_memory()
    manager.free(addr)
    manager.display_memory()

def test_merge_free_blocks():
    print("=== Test: Merge Free Blocks ===")
    manager.merge_free_blocks()
    manager.display_memory()
    result = manager.display_memory() # Displays the memory status after freeing the block.
    print(result)

def test_get_statistics(): # You need to run it and actually see the printed statistics to verify it works.
    print("=== Test: Get Statistics ===")
    result = manager.get_statistics()
    print(result)
    manager.display_memory()

if __name__ == '__main__':
    test_memory_initialization()
    test_allocation()
    test_free(0)
    test_merge_free_blocks()
    test_allocation()
    test_get_statistics()
