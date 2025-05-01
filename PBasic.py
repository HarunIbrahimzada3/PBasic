from array import array
import matplotlib.pyplot as plt
import numpy as np
import math
class PExecute:
    def __init__(self):
        self.ilibrary = self.ILibrary()
        self.slibrary = self.SLibrary()
        self.elseif = self.ElseIf()
        self.interrupt_handler = self.InterruptHandler()
        
        # Инициализация регистров. Теперь это могут быть любые значения.
        self.registers = {
            "AX": None, # Регистр AX 
            "BX": 0,  # Регистр BX
            "KX": 0,  # Регистр KX
            "XX": None,  # Регистр XX
            "YX": None,  # Регистр YX
        }
        
        # Экземпляр класса __reg__ для работы с регистрами
        self.reg = self.__reg__(self.registers)
        
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

        def Vif(self, Arg1, Arg2):
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
        
        def zerozero(self, *args, **kwargs):
            return self
        
        def zeroone(self, arg, *args, **kwargs):
            if len(arg) > 0:
                print(True)
            else:
                print(False)

    class __reg__:
        def __init__(self, registers):
            # Привязка к внешнему словарю регистров
            self.registers = registers
        
        def make(self, register_name, initial_value=None):
            
            self.registers[register_name] = initial_value

        def read(self, register_name):
            
            if register_name in self.registers:
                return self.registers[register_name]
            else:
                raise ValueError(f"Register '{register_name}' does not exist.")

        def write(self, register_name, value):
            
            if register_name in self.registers:
                self.registers[register_name] = value
            else:
                raise ValueError(f"Register '{register_name}' does not exist.")
class graph:
    def __init__(self,reg):
        self.reg = reg
    def draw_graph(self):
        K = self.reg.read("KX")  
        B = self.reg.read("BX")
        x_values = list(range(-100, 110))
        y_values = [K * x + B for x in x_values]

        plt.plot(x_values, y_values, label=f"y = {K}x + {B}")
        
        plt.title("Graph of y = KX + B")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()
        
class PMath:
    def __init__(self):
        pass
# Учтите, функция tan , cos и sin принимают только значения РАДИАН, не градусов! 
    def tan(self,arg):
        check1 = isinstance(arg,(float,int))
        if check1:
           return math.tan(arg)
    def cos(self,arg):
        
        check1 = isinstance(arg,(float, int))
        if check1:
            return math.cos(arg)
    def sin(self,arg):
        
        check1 = isinstance(arg,(int, float))
        if check1:
            return math.sin(arg) 
