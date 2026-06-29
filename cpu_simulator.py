# --- MY 2025 CPU HARDWARE SIMULATION ---
# Built after my sophomore year to figure out how computer chips actually work.
# This script takes my own text commands, turns them into numbers, and runs them.

# Simulating the physical hardware parts using basic variables
register_A = 0    # First storage slot on the chip
register_B = 0    # Second storage slot on the chip
pc = 0            # Program Counter (tracks which instruction line we are on)
ram = [0] * 16    # 16 slots of total computer memory storage
running = True

def my_compiler(text_program):
    """Turns my custom text commands into simple instruction numbers."""
    number_program = []
    
    for line in text_program:
        parts = line.split()
        if not parts:
            continue
        command = parts[0]
        
        # Mapping text to number codes (Opcodes)
        if command == "LOAD_A":
            number_program.append(1)
            number_program.append(int(parts[1])) # The number value to load
        elif command == "LOAD_B":
            number_program.append(2)
            number_program.append(int(parts[1])) # The number value to load
        elif command == "ADD":
            number_program.append(3)
            number_program.append(0) # Padding because ADD doesn't need an extra number
        elif command == "STORE_A":
            number_program.append(4)
            number_program.append(int(parts[1])) # The RAM slot number
        elif command == "HALT":
            number_program.append(5)
            number_program.append(0) # Padding
            
    return number_program

def run_cpu(machine_code):
    """The main loop that mimics a physical computer processor cycle."""
    global register_A, register_B, pc, running
    
    print("--- STARTING CORE CHIP SIMULATION ---")
    
    while running and pc < len(machine_code):
        # 1. Grab the instruction and its paired value
        opcode = machine_code[pc]
        argument = machine_code[pc + 1]
        
        # 2. Decode the number and execute the hardware action
        if opcode == 1:   # LOAD_A
            register_A = argument
            print(f"[HW STATE] Loaded value {argument} into Register A")
            pc += 2
            
        elif opcode == 2: # LOAD_B
            register_B = argument
            print(f"[HW STATE] Loaded value {argument} into Register B")
            pc += 2
            
        elif opcode == 3: # ADD
            register_A = register_A + register_B
            print(f"[ALU MATH] Added B to A. Register A is now: {register_A}")
            pc += 2
            
        elif opcode == 4: # STORE_A
            ram_slot = argument
            ram[ram_slot] = register_A
            print(f"[RAM WRITE] Saved Register A value ({register_A}) into RAM slot {ram_slot}")
            pc += 2
            
        elif opcode == 5: # HALT
            print("[SYSTEM] HALT command received. Stopping simulation.")
            running = False
            
        else:
            print(f"🚨 ERROR: Glitched instruction code: {opcode}")
            running = False

# --- TESTING MY CODE ---
# A basic program to calculate 5 + 10 and save the result to memory
my_writing = [
    "LOAD_A 5",   # Put 5 in slot A
    "LOAD_B 10",  # Put 10 in slot B
    "ADD",        # Add slots together (5 + 10 = 15)
    "STORE_A 3",  # Save the answer 15 into RAM slot 3
    "HALT"        # Turn off the system
]

# Run the compiler and start the CPU loop
compiled_numbers = my_compiler(my_writing)
run_cpu(compiled_numbers)

# Print out what the physical hardware looks like at the end
print("\n--- FINAL CHIP SNAPSHOT ---")
print(f"Register A: {register_A}")
print(f"Register B: {register_B}")
print(f"RAM Grid: {ram}")

