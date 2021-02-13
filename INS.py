import ALU
import RAM
import ROM
import time
import threading

# INSTABLE
# 0000 NOP
# 0001 LDA
# 0010 LDB
# 0011 STA
# 0100 STB
# 0101 STO
# 0110 LDAN
# 0111 LDBN
# 1000 ADD
# 1001 SUB
# 1010 JMP
# 1111 HALT

# REGISTERS
RAD  = "0000"     # A           Regsiter (ALU) [4]
RBD  = "0000"     # B           Register (ALU) [4]
LRD  = "0000"     # Line        Register (INS) [4]
INSR = "00000000" # Instruction Register (INS) [8]
ROD  = "0000"     # Output      Register (ALU) [4]
STEP = "0000"     # Step        Register (INS) [4]

# CONSTANTS
LOOP = False

# FUNCTIONS
def Start(Speed):
    global LOOP
    LOOP = True
    CLKS = Speed
    while LOOP:
        OUTPUT = INFLOOP()
        if not OUTPUT:
            break
        time.sleep(CLKS)

def INFLOOP():
    global LOOP
    # DEFINITONS
    OPERATION = "NONE"
    global RAD
    global RBD
    global LRD
    global INSR
    global ROD
    global STEP
    INSR = ROM.Read(LRD)
    OPCODE = INSR[0] + INSR[1] + INSR[2] + INSR[3]
    OPERAND = INSR[4] + INSR[5] + INSR[6] + INSR[7]

    # INSTRUCTIONS
    if OPCODE == "0000":
        ERR = "OK"
        OPERATION = "NONE"
    elif OPCODE == "0001":
        ERR = "OK"
        OPERATION = "LDA"
        RAD = RAM.Read(OPERAND)
    elif OPCODE == "0010":
        ERR = "OK"
        OPERATION = "LDB"
        RBD = RAM.Read(OPERAND)
    elif OPCODE == "0011":
        ERR = "OK"
        OPERATION = "STA"
        RAM.Write(OPERAND, RAD)
    elif OPCODE == "0100":
        ERR = "OK"
        OPERATION = "STB"
        RAM.Write(OPERAND, RBD)
    elif OPCODE == "0101":
        ERR = "OK"
        OPERATION = "STO"
        RAM.Write(OPERAND, ROD)
    elif OPCODE == "0110":
        ERR = "OK"
        OPERATION = "LDAN"
        RAD = OPERAND
    elif OPCODE == "0111":
        ERR = "OK"
        OPERATION = "LDBN"
        RBD = OPERAND
    elif OPCODE == "1000":
        ERR = "OK"
        OPERATION = "ADD"
        ROD = ALU.Add4(RAD, RBD)['OUT']
    elif OPCODE == "1001":
        ERR = "OK"
        OPERATION = "SUB"
        ROD = ALU.Sub4(RAD, RBD)['OUT']
    elif OPCODE == "1010":
        ERR = "OK"
        OPERATION = "JMP"
        LRD = OPERAND
    elif OPCODE == "1111":
        ERR = "OK"
        OPERATION = "END"
        LOOP = False
    else:
        ERR = "OPCODEERR"
        OPERATION = "UNKOWN"

    print('__________________')
    print('\nREGISTER INFO\n')
    print('RAD      | '+RAD)
    print('RBD      | '+RBD)
    print('LRD      | '+LRD)
    print('INSR     | '+INSR)
    print('ROD      | '+ROD)
    print('STEP     | '+STEP)
    print('\nOPERATION INFO\n')
    print('OP       | '+INSR)
    print('OPCODE   | '+OPCODE)
    print('OPERAND  | '+OPERAND)
    print('INS      | '+OPERATION)
    print('\nRAM INFO\n')
    COUNTERD = "0000"
    COUNTERF = ""
    OP = {'FLAG': 'OK', 'OUT': '0000'}
    while COUNTERF != "OVERFLOW":
        COUNTERF = OP['FLAG']
        COUNTERD = OP['OUT']
        print(COUNTERD+' : '+RAM.Read(COUNTERD))
        if COUNTERD == "1111":
            break
        else:
            OP = ALU.Add4(COUNTERD, "0001")

    if not LOOP:
        print('\n')
    else:
        if OPERATION != "JMP":
            LRD = ALU.Add4(LRD, "0001")['OUT']

    return LOOP
