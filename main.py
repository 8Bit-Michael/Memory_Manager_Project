while __name__ == "__main__":
    from memory_manager import MemoryManager
    from difflib import get_close_matches

    def match_input(user_input, options, cutoff=0.6):
        return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)
    
    manager = MemoryManager(1024)
    while True:   
        command = input("Enter command allocate <size>, free <address>, display, or exit:").strip().lower()
        
        if command.startswith("allocate"): # If you chose to allocate
            try:
                _, size_str = command.split() # Split the command into two parts
                size = int(size_str) # Convert the size part to an integer
                address = manager.allocate(size)
                if address is not None: # if the chosen address of the allocation was successful:
                    print(f"Allocated {size} bytes at address {address}") # Print the address of the allocated block.
                else: # If the allocation failed:
                    print("Allocation failed. Not enough memory.")

            except (ValueError, IndexError):
                print("Invalid command. Usage: allocate <size>") 

        elif command.startswith("free"): # If you chose to free 
            try:
                _, address_str = command.split() # Split the command into two parts
                address = int(address_str) # Convert the address part to an integer
                manager.free(address)
                print(f"Freed memory at address {address}")

            except (ValueError, IndexError):
                print("Invalid command. Usage: free <address>")

        elif command == "display": # If you chose to display the results
            result = manager.display_memory()
            print(result)

        elif command == "exit": # If you chose to exit:
            print("Exiting memory manager.")
            break

        else:
            matched = match_input(command, ["allocate", "free", "display", "exit"])
            if matched:
                print(f"Did you mean '{matched[0]}'? Please try again.")
            else:
                print("Unknown command. Please try again.")
