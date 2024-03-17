P1 = [0b1011100001100100, 0b0111100000000000, 0b1011000011111111,
      0b0111000000000000, 0b1001111100000100, 0b0001111101100000,
      0b1101100000001000, 0b1100000000001001, 0b0010100110100000,
      0b0010011001100000, 0b1101100000001010, 0b0010000110000000,
      0b1100000000000100, 100, 100]
'''
0: R7 = 100
1: R7 = -R2   # Set R7 to -100 for testing convenience = 0
2: R6 = 255
3: R6 = -R6   # Set R6 to -255 (terminating condition for processor memory limit)
4: R3 = P[R4]  # R4 is a pointer traversing P from 0 to 255
5: R3 = R3 + R7   # Add R7 to R3
6: if R3 = 0 jump to 8   # Jump to 8 if 100 is found in P
7: else jump to 9   # Jump to 9 if the element is not 100
8: R5 = R5 + R1   # Increment R5 (count of occurrences of 100)
9: R3 = R4 + R6   # Set R3 (or another register) to R4 (pointer) - 255
10: if R3 = 0 jump to 10   # If R3 is 0, the traversal of P is complete, go to 10 (END)
11: R4 = R4 + R1   # Increment R4, continue traversing
12: jump to 4   # Repeat from 4
'''

# 32 bit registers
R = [0b0 for x in range(8)]

# 16 bit program memory
P = [0b0 for x in range(256)]

# 32 bit adder
Adder = []

# 8 bit program counter
pc = 0

# Initialize some constants in registers
R[0] = 0  # constant in R(0)
R[1] = 1  # constant in R(1)

# Initialize variables a, b, c
a = 0
b = 0
c = 0

# Load a program into memory
P[0:len(P1)] = P1  # Assuming P1 is previously defined
P[100] = 100
P[255] = 100

# Main execution loop
while True:
    inst = P[pc]  # Fetch the instruction at the program counter
    print(pc, R)  # Print the current program counter and register values
    pc = pc + 1  # Increment program counter for the next iteration

    # Extract operation code from the instruction
    operation = inst >> 14

    # Decode and execute instructions based on the operation code
    if operation == 0b00:  # add
        a = (inst & 0b0011100000000000) >> 11
        b = (inst & 0b0000011100000000) >> 8
        c = (inst & 0b0000000011100000) >> 5
        R[c] = R[a] + R[b]

    elif operation == 0b01:  # neg
        a = (inst & 0b0011100000000000) >> 11
        R[a] = (-1) * R[a]

    elif operation == 0b10:  # lod
        a = (inst & 0b0011100000000000) >> 11
        b = (inst & 0b0000011100000000) >> 8
        if b == 0:  # const
            c = (inst & 0b0000000011111111)
            R[a] = c
        else:  # memory
            c = (inst & 0b0000000000000111)
            R[a] = P[R[c]]

    elif operation == 0b11:  # jiz
        a = (inst & 0b0011100000000000) >> 11
        b = (inst & 0b0000000011111111)
        if R[a] == 0:
            pc = b  # Jump if R[a] is zero
