import matplotlib.pyplot as plt

class PExecute:
    def __init__(self):
        self.registers = {
            "AX": None,  # Регистр AX
            "BX": None,  # Регистр BX
            "KX": 1,     # Коэффициент наклона, начальное значение
            "XX": None,  # Регистр XX
            "YX": None,  # Регистр YX
        }
        
        self.reg = self.__reg__(self.registers)
        
    class __reg__:
        def __init__(self, registers):
            self.registers = registers
        
        def make(self, register_name, initial_value=None):
            """Создаёт новый регистр с начальным значением."""
            self.registers[register_name] = initial_value

        def read(self, register_name):
            """Чтение значения регистра."""
            if register_name in self.registers:
                return self.registers[register_name]
            else:
                raise ValueError(f"Register '{register_name}' does not exist.")

        def write(self, register_name, value):
            """Запись значения в регистр."""
            if register_name in self.registers:
                self.registers[register_name] = value
            else:
                raise ValueError(f"Register '{register_name}' does not exist.")
    
    def draw_graph(self):
        """Функция для рисования графика y = Kx + B"""
        K = self.reg.read("KX")  # Коэффициент наклона из регистра KX
        B = self.reg.read("BX")  # Сдвиг по оси Y из регистра BX
        
        # Генерация значений X (например, от -10 до 10)
        x_values = list(range(-10, 11))  # Значения X от -10 до 10
        
        # Вычисление значений Y по формуле y = Kx + B
        y_values = [K * x + B for x in x_values]
        
        # Построение графика
        plt.plot(x_values, y_values, label=f"y = {K}x + {B}")
        
        plt.title("Graph of y = Kx + B")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()

# Пример использования:
exec = PExecute()

# Устанавливаем значения регистров
exec.reg.write("KX", 2)  # Коэффициент наклона (K)
exec.reg.write("BX", 3)  # Сдвиг по оси Y (B)

# Рисуем график
exec.draw_graph()
