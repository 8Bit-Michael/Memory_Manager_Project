from memory_manager import MemoryManager

def test_memory_initialization():
    manager = MemoryManager(1024)
    assert manager.total_size == 1024
    assert manager.head.size == 1024
    assert manager.head.is_free is True
    assert manager.head.start == 0
    assert manager.head.next is None
    if manager.head.memory_block == manager: # Confirming the linked list node points back to the MemoryManager instance.
        print("Memory block correctly linked to MemoryManager instance, size of memory:", manager.head.size)

test_memory_initialization()
