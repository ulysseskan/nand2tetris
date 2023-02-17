"""Multiply 1 or 2 negative numbers using only addition & subtraction.
   (prep for translating into assembly in nand2tetris course)
"""
R0 = -3
R1 = 5

COUNT = abs(R1)
SUM = abs(0)

def is_neg(num):
    """ lambda expression adapted from https://stackoverflow.com/a/48677136 """
    return str(num)[0]=='-' and len(str(num))>1

if is_neg(R0) and is_neg(R1):
    while COUNT != 0:
        SUM = SUM + R0
        COUNT = COUNT - 1

elif is_neg(R0) is False and is_neg(R1) is True:
    while COUNT != 0:
        SUM = SUM + R0
        COUNT = COUNT - 1
    SUM = -abs(SUM)

else:
    while COUNT != 0:
        SUM = SUM + R0
        COUNT = COUNT - 1

R2 = SUM
print('R2:', R2)
