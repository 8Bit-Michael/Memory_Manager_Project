from memory_manager import MemoryManager

def test_memory_initialization():
    manager = MemoryManager(1024)
    assert manager.total_size == 1024
    assert manager.head.size == 1024
    assert manager.head.is_free is True
    assert manager.head.start == 0
    assert manager.head.next is None
    while manager.head:
        print(f"Block Start: {manager.head.start}, Size: {manager.head.size}, Is Free: {manager.head.is_free}")
        manager.head = manager.head.next

test_memory_initialization()

