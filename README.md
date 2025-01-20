# memory-allocator
A memory allocator written in assembly 86 and wrapped in python
# Memory Allocator: Assembly x86 Wrapped in Python

## Overview

This project is a memory allocator implemented in x86 Assembly, designed for low-level memory management tasks. The core allocator is wrapped in Python, providing a user-friendly interface to leverage its functionality in high-level applications.

## Features

- **Low-Level Control**: Efficient memory allocation and deallocation using x86 Assembly.
- **Python Interface**: Simplifies usage and integration with Python applications.
- **Custom Memory Pools**: Allows users to manage memory in predefined regions for optimal performance.
- **Platform-Specific Optimization**: Tailored for systems that support x86 architecture.

## Getting Started

### Prerequisites

- A system capable of running x86 Assembly code.
- Python 3.8 or later.
- An assembler like `NASM` or `MASM` to build the Assembly code.
- `ctypes` or a similar Python library for interfacing with the Assembly code.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/memory-allocator.git
   cd memory-allocator
Assemble the x86 code:
nasm -f elf32 allocator.asm -o allocator.o
ld -m elf_i386 -shared -o allocator.so allocator.o

Install Python dependencies (if any):

pip install -r requirements.txt
Run the Python wrapper:

python example.py
Usage
Python Interface
Import the memory allocator wrapper and use its methods:

python
from allocator import MemoryAllocator

# Initialize allocator with a memory pool size
allocator = MemoryAllocator(pool_size=1024)

# Allocate memory
ptr = allocator.allocate(128)
print(f"Allocated memory at: {ptr}")

# Free memory
allocator.free(ptr)
print("Memory freed.")
Assembly Module
The Assembly module exposes low-level functions for:

Allocating memory
Freeing memory
Managing memory pools
Refer to the allocator.asm file for detailed comments and implementation.

Example
An example script, example.py, demonstrates the usage of the allocator in Python. Run it to see the allocator in action.

python example.py

Assembly Code: See allocator.asm for detailed implementation of the allocator.
Python Wrapper: Check allocator.py for the interface and integration details.
Examples: Example scripts are located in the examples/ directory.
Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Inspired by low-level memory management techniques.
Thanks to the open-source community for Python and Assembly resources.
