# cpu-simulator

# My 2025 CPU Simulator Project

A simple Python program I wrote after my sophomore year to teach myself how computer chips read binary instructions and manage memory at a low level.

## Why I Built This
In 2025, after taking introductory coding classes, I realized I had no idea how a physical computer actually executes code. We always write high-level words, but chips only understand numbers. I wanted to see what the bridge looked like between software text and physical memory slots.

This script builds a virtual computer chip using basic Python variables and lists. It reads a custom text language I made up, turns those commands into code numbers, and loops through them just like a real processor.

## Project Features
1. **Basic Compiler**: Takes simple text strings like `LOAD_A` and converts them into numeric codes that the simulation loop can handle.
2. **Virtual Registers**: Uses standard integer variables (`register_A` and `register_B`) to act as temporary storage pins right on the simulated chip.
3. **The Chip Loop**: Mimics the classic hardware cycle by grabbing a code number, reading the argument value, changing the variables, and updating the program counter.
4. **RAM Grid**: Uses a 16-slot Python list to act as a bare-minimum hard drive memory layout.

