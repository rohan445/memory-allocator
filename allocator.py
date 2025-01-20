import ctypes
import os

# Compile the assembly x86 code into a shared library
def compile_assembly():
    asm_file = "allocator.asm"
    obj_file = "allocator.o"
    shared_lib = "allocator.so"

    # Assemble the Assembly file into an object file
    os.system(f"nasm -f elf64 {asm_file} -o {obj_file}")
    # Link the object file into a shared library
    os.system(f"gcc -shared -o {shared_lib} {obj_file}")

# Wrapping the assembly code 
class MemoryAllocator:
    def __init__(self):
        # Load the shared library
        self.lib = ctypes.CDLL("./allocator.so")
        # Bind Assembly functions
        self.allocate_memory = self.lib.allocate_memory
        self.free_memory = self.lib.free_memory
        self.allocate_memory.restype = ctypes.c_void_p  # Pointer to memory

    def allocate(self):
        # Call the allocate_memory function
        return self.allocate_memory()

    def free(self):
        # Call the free_memory function
        self.free_memory()

# Main function
if __name__ == "__main__":
    # Compile the Assembly code
    compile_assembly()

    # Use the memory allocator
    allocator = MemoryAllocator()

    # Allocate memory
    memory_pointer = allocator.allocate()
    print(f"Memory allocated at address: {hex(memory_pointer)}")

    # Free memory
    allocator.free()
    print("Memory freed successfully.")
