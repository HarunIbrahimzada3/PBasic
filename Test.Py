
from PBasic import *
PEint = PExecute.InterruptHandler()
PE = PExecute()
PE.ilibrary.Add(5)
PEint.int_call(0x01, PE.ilibrary)
