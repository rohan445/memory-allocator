section .data
    ; Set Size of the allocated block
    block_size dq 1024    ; 1KB taken 

section .bss
    memory_block resb 1024 

section .text
    global allocate_memory
    global free_memory

allocate_memory:
    ; Input: None
    ; Output: RAX = Pointer pointing to the memory block
    mov rax, memory_block
    ret

free_memory:
    ; Input: None
    ; Reset the memory block
    mov rdi, memory_block
    mov rcx, 1024          ; Block size
    xor rax, rax           ; Fill with zeros
    rep stosb
    ret
