ROP_DEST = 0x14655D60 - 0x4
ROP_OFFSET_KSN = 0xEF1AC

MOV_SP_R0_MOV_R0R2_MOV_LRR3_BX_R1 = 0x148938

NOP = 0x142390

POP_R4LR_BX_R1 = 0x102190
POP_R0PC = 0x2420B8
POP_R1PC = 0x24C158
POP_R3PC = 0x103C00
POP_R4PC = 0x100270
POP_R11PC = 0x129714
POP_R4R5PC = 0x100A90
POP_R4R6PC = 0x29FA40
POP_R0R1R2R3R4PC = 0x15545C
POP_R1R2R3R4R5PC = 0x320E34
POP_R1R2R3R4R5R6R7PC = 0x158058
POP_R3R4R5R6R7R8R9PC = 0x2CEE4C
POP_R4R5R6R7R8R9R10R11PC = 0x13919C
POP_R4R5R6R7R8R9R10R11R12PC = 0x2DD908

LDR_R0R0_POP_R4PC = 0x1338A8
LDR_R0R0_STR_R0R1_POP_R4PC = 0x115E30
STR_R0R1_POP_R4PC = LDR_R0R0_STR_R0R1_POP_R4PC+0x4
STRB_R0R4_POP_R4PC = 0x100CB0

ADD_R0R0R4_POP_R4PC = 0x249E88

SUB_SPSPR3_MOV_R1SP_STR_R3SP_MIN4INC_BLX_R2 = 0x143D8C

CMP_R0R1_MOVGT_R0_1_MOVLE_R0_0_POP_R4PC = 0x21D3B8

STREQ_R0R4_2C_POP_R4PC = 0x2587A4

LMSI_MEMCMP = 0x1344EC

GSPGPU_GXTRYENQUEUE = 0x24A304
GSPGPU_GXTRYENQUEUE_WRAPPER = 0x12B258
GSPGPU_FLUSHDATACACHE_WRAPPER = 0x12B348
GSPGPU_FLUSHDATACACHE = 0x1308BC
GSPGPU_GXCMD4 = 0x12B448
GSPGPU_INTERRUPT_RECEIVER_STRUCT = 0x003A6C40
GSPGPU_HANDLE = 0x3C7D0C

FS_MOUNTSDMC = 0x25F800
FS_TRYOPENFILE = 0x25EE14
FS_TRYGETSIZE = 0x25EDBC
FS_CLOSEFILE = 0x25EEA8
FS_TRYREADFILE = 0x10E3D0
FSUSER_HANDLE = 0x3B6430

DSP_UNLOADCOMPONENT = 0x11DE30
DSP_REGISTERINTERRUPTEVENTS = 0x11DEFC
DSP_HANDLE = 0x3B63E4

SVC_SLEEPTHREAD = 0x24C168
SVC_EXITTHREAD = 0x11BF88

MAIN_THREAD_BREAK = 0x154D9D00 + 0x8
MAIN_THREAD_POP_PTR = 0x0FFFFCE4

THREAD1_BREAK = 0x3A6C40 + 0x77
