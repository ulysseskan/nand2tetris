"""Write python code for multiplying 2 positive integers
using ONLY addition and subtraction.  Purpose is to
translate the python code into assembly language.

Multiplies R0 and R1 and stores the result in R2.
(R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

This program only needs to handle arguments that satisfy
R0 >= 0, R1 >= 0, and R0*R1 < 32768.
"""

R0 = 6
R1 = 7

COUNT = R1
SUM = 0

while COUNT != 0:
    SUM = SUM + R0
    COUNT = COUNT - 1
R2 = SUM
print('SUM:', R2)
