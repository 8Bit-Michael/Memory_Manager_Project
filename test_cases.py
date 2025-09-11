
def test_memory_initialization():
    print("=== Test: Memory Initialization ===")
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
    manager = MemoryManager(1024)
    manager.allocate(300)
    manager.display_memory()
    print()

if __name__ == '__main__':
    test_memory_initialization()
    test_allocation()

