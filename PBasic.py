from array import array

class PMath:
    def __init__(self, argument):
        self.argument = argument

    def PrintLn(self):
        print(self.argument)
    def Mul(self, argumentMul):
        print(float(self.argument * argumentMul))
    def Div(self, argumentDiv):
        print(float(self.argument / argumentDiv))
    def Plus(self, argumentPlus):
        print(float(self.argument + argumentPlus))
    def Minus(self, argumentMinus):
        print(float(self.argument - argumentMinus))
class PExecute:
    def __init__(self):
        self.ilibrary = self.ILibrary()
        self.slibrary = self.SLibrary()
        self.elseif = self.ElseIf()
        self.interrupt_handler = self.InterruptHandler()
        
    class ILibrary:
        def __init__(self):
            self.ILibrary = array('i', [])
        def __len__(self):
            return len(self.ILibrary)
        def Add(self, argumentAdd):
            self.ILibrary.append(argumentAdd)

        def Show(self):
            print(self.ILibrary)

    class SLibrary:
        def __init__(self):
            self.SLibrary = array('u', [])
            
        def Add(self, argumentAdd):
            self.SLibrary.append(argumentAdd)
        def Show(self):
            print(self.SLibrary)

    class ElseIf:
        def __init__(self):
            return

        def Vif(self,Arg1,Arg2):
            if isinstance(Arg1, int) and isinstance(Arg2, int):
                if Arg1 > Arg2:
                    return Arg1
                elif Arg1 < Arg2:
                    return Arg2
                else:
                    print("Error! ==")
            else:
                print("Error!")

    class InterruptHandler:
        def __init__(self):
            self.interrupt_table = {
                0x00: self.zerozero,
                0x01: self.zeroone
            }

        def register_interrupt(self, interrupt_number, handler):
            self.interrupt_table[interrupt_number] = handler

        def int_call(self, interrupt_number, *args, **kwargs):
            if interrupt_number in self.interrupt_table:
                return self.interrupt_table[interrupt_number](*args, **kwargs)
            else:
                raise Exception(f"Unknown interrupt: {interrupt_number}")
        
        def zerozero(self, *args , **kwargs):
            return self
        
        def zeroone(self, arg, *args , **kwargs):
            if len(arg) > 0:
                print(True)
            else:
                print(False)
        