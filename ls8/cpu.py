"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    LDI = 0b10000010
    PRN = 0b01000111
    HLT = 0b00000001


    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.regulator = [0] * 8
        self.pc = 0
        # need to set up functionality needs

    def ram_read(self, ram_address):
        ram_value = self.ram[ram_address]
        return ram_value

    def ram_write(self, ram_value, ram_address):
        self.ram[ram_address] = ram_value


    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:
            hard_code = self.ram_read(self.pc)

            if hard_code == LDI:
               next_index_a = self.ram_read(self.pc + 1)
               next_index_b = self.ram_read(self.pc + 2)

