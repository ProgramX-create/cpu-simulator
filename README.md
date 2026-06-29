# cpu-simulator

# My 2025 CPU Simulator Project

A simple Python program I wrote during my sophomore year to teach myself how computer chips read binary instructions and manage memory at a low level.

## Why I Built This
In 2025, after taking my first classes of AP Computer Science Principles, I realized I had no idea how a physical computer actually executes code.
So I put two and two togther the class was teaching JavaScript but I already knew Python. So I said let's do this.




## Project Features
1. **Basic Compiler**: Takes simple text strings like `LOAD_A` and converts them into numeric codes that the simulation loop can handle.
2. **Virtual Registers**: Uses standard integer variables (`register_A` and `register_B`) to act as temporary storage pins right on the simulated chip.
3. **The Chip Loop**: Mimics the classic hardware cycle by grabbing a code number, reading the argument value, changing the variables, and updating the program counter.
4. **RAM Grid**: Uses a 16-slot Python list to act as a bare-minimum hard drive memory layout.

